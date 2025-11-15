from data_structures import ArrayR
from data_structures import linked_stack
from processing_line import Transaction
class Entry : 
    __slots__ = ("tx","sig","amount")

    def __init__(self,tx,amount):
        self.tx = tx 
        self.sig = tx.signature 
        self.amount = amount 

class ProcessingBook:
    LEGAL_CHARACTERS = "abcdefghijklmnopqrstuvwxyz0123456789"

    def __init__(self, level:int = 0):
        self.pages = ArrayR(len(ProcessingBook.LEGAL_CHARACTERS))
        self._level = level 
        i = 0 
        while i <36: 
            self.pages[i] = None 
            i += 1 
        self._errors = 0 
        self._size = 0 
    
    def page_index(self, character):
        """
        You may find this method helpful. It takes a character and returns the index of the relevant page.
        Time complexity of this method is O(1), because it always only checks 36 characters.
        """
        return ProcessingBook.LEGAL_CHARACTERS.index(character)
    
    def __setitem__(self,tx,amount):
        sig = tx.signature 
        if sig is None: 
            raise ValueError("Transaction must signed before inserting into ProcessingBook")
        idx_char = sig[self._level]
        idx = self.page_index(idx_char)
        slot = self.pages[idx]
        if slot is None : 
            self.pages[idx] = Entry(tx,amount)
            self._size += 1 
            return       
        if isinstance(slot,Entry):
            if slot.sig == sig : 
                if slot.amount != amount : 
                    self._errors += 1 
                return
            child = ProcessingBook(self._level + 1)
            child[slot.tx] = slot.amount 
            child[tx] = amount 
            self.pages[idx] = child 
            self._size += 1 
            return 
        before = slot._size 
        slot.__setitem__(tx,amount)
        after = slot._size
        if after > before:
            self._size += 1
        
    
    def __getitem__(self,tx):
        sig = tx.signature 
        if sig is None: 
            raise ValueError("Unsigned transaction not found")
        idx_char = sig[self._level]
        idx = self.page_index(idx_char)
        slot = self.pages[idx]
        if slot is None: 
            raise KeyError("Transaction is not found")
        if isinstance(slot,Entry):
            if slot.sig == sig : 
                return slot.amount 
            raise KeyError("Transaction not found")
        return slot[tx]
            
    def get_error_count(self):
        """
        Returns the number of errors encountered while storing transactions.
        """
        total = self._errors
        for page in self.pages:
            if isinstance(page, ProcessingBook):
                total += page.get_error_count()
        return total
    
    def __delitem__(self,tx):
        sig = tx.signature 
        if sig is None: 
            raise ValueError("Unsigned transaction cannot be deleted")
        idx = self.page_index(sig[self._level])
        slot = self.pages[idx]
        
        if slot is None:
            raise KeyError("Transaction not found")
        
        if isinstance(slot,Entry):
            if slot.sig == sig: 
                self.pages[idx] = None
                self._size -= 1
                return 
            raise KeyError("Transaction not found")
        
        before = slot._size 
        slot.__delitem__(tx)
        after = slot._size 
        if after < before: 
            self._size -= 1 
            
        count  = 0 
        lone = None 
        i = 0 
        while i < 36:
            c = slot.pages[i]
            if c is not None:
                lone = c 
                count += 1
            i += 1 
        if count == 0 :
            self.pages[idx]= None
        elif count == 1 and isinstance(lone,Entry):
            self.pages[idx] = lone
    
    def __len__(self):
        return self._size 
    
    def __iter__(self):
        return PBIter(self)
    

    
    def sample(self, required_size):
        """
        1054 Only - 1008/2085 welcome to attempt if you're up for a challenge, but no marks are allocated.
        Analyse your time complexity of this method.
        """
        pass

class StackNode :
    __slots__ = ("book", "next_idx","prev")
    def __init__(self,book,next_idx,prev):
        self.book = book
        self.next_idx = next_idx
        self.prev = prev 
    
class PBIter:
    __slots__ = ("cur","i","stack")
    def __init__(self,root):
        self.cur = root 
        self.i = -1
        self.stack = linked_stack.LinkedStack()
    def __iter__(self):
        return self 
    def __next__(self):
        while True :
            self.i += 1 
            while self.i < 36 :
                slot = self.cur.pages[self.i]
                if slot is None : 
                    self.i += 1
                    continue
                if isinstance(slot,Entry):
                    tx = slot.tx 
                    amt = slot.amount
                    self.i += 1 
                    return (tx,amt)
                self.stack.push((self.cur, self.i + 1))
                self.cur = slot
                self.i = 0 

            if self.stack.is_empty() : 
                raise StopIteration
            parent_book, next_idx = self.stack.pop()
            self.cur = parent_book
            self.i = next_idx - 1
    

# test_deep_collapse_large_fixed.py
import random, string
from processing_line import Transaction
from processing_book import ProcessingBook, Entry

ALPHABET = "abcdefghijklmnopqrstuvwxyz0123456789"

def mk_tx(uid, sig):
    t = Transaction(uid, "s", "r")
    t.signature = sig
    return t

def random_sig(n, disallow_first=None):
    chars = string.ascii_lowercase + string.digits
    while True:
        s = "".join(random.choice(chars) for _ in range(n))
        if not disallow_first or s[0] not in disallow_first:
            return s

if __name__ == "__main__":
    random.seed(123)

    # -----------------------------
    # CONFIG
    # -----------------------------
    COMMON_PREFIX_LEN = 40     # depth of forced nesting
    GROUPS = 10                # number of deep-collision groups
    GROUP_SIZE = 40            # 39 will be deleted, 1 survives
    RANDOM_FILL = 1200         # extra noise, but we exclude group start letters
    TOTAL = GROUPS * GROUP_SIZE + RANDOM_FILL

    # 1) Choose GROUPS distinct start letters for deep groups
    start_letters = random.sample(list(string.ascii_lowercase), GROUPS)

    print(f"Building {TOTAL} transactions...")
    book = ProcessingBook()
    uid = 1

    # 2) Insert RANDOM_FILL noise that explicitly avoids the groups' first letters
    for _ in range(RANDOM_FILL):
        sig = random_sig(16, disallow_first=set(start_letters))
        tx = mk_tx(uid, sig); uid += 1
        book[tx] = random.randint(1, 10000)

    # 3) Build GROUPS of deep-collision signatures with exclusive top-level pages
    deep_groups = []
    for g, first_char in enumerate(start_letters):
        prefix = first_char * COMMON_PREFIX_LEN   # long common prefix
        group_txs = []
        for k in range(GROUP_SIZE):
            # ensure uniqueness after prefix; diverge late to force deep nesting
            tail = f"{g:02d}{k:02d}"
            sig = prefix + tail
            tx = mk_tx(uid, sig); uid += 1
            amt = random.randint(1, 10000)
            book[tx] = amt
            group_txs.append((tx, amt))
        deep_groups.append((first_char, group_txs))

    print("Inserted:", len(book))

    # 4) In each group, delete all but one to force collapse
    survivors = []
    for first_char, group in deep_groups:
        survivor_tx, survivor_amt = group[-1]
        for tx, _ in group[:-1]:
            del book[tx]
        survivors.append((first_char, survivor_tx, survivor_amt))

    print("After collapsing groups, size:", len(book))

    # 5) Verify each survivor is a direct Entry at its exclusive top-level page
    failures = 0
    for first_char, tx, amt in survivors:
        idx = book.page_index(first_char)
        slot = book.pages[idx]
        if isinstance(slot, Entry):
            if slot.tx.signature != tx.signature or slot.amount != amt:
                print(f"[FAIL] Direct Entry mismatch at top-level page '{first_char}'")
                failures += 1
        else:
            # Not fully collapsed at top level → failure in this exclusive setup
            print(f"[FAIL] Not fully collapsed at top-level page '{first_char}'")
            failures += 1

    if failures == 0:
        print("Deep collapse check (exclusive pages): PASSED for all groups ✅")
    else:
        print(f"Deep collapse check (exclusive pages): FAILED on {failures} group(s) ❌")

    # 6) Sanity: iterator order (a..z then 0..9)
    rank = {c: i for i, c in enumerate(ALPHABET)}
    def sig_key(s): return tuple(rank[c] for c in s)
    sigs = [t.signature for (t, a) in book]
    assert sigs == sorted(sigs, key=sig_key), "Iterator/page order mismatch"
    print("Iterator/page order OK ✅")

    # 7) Sanity: survivor lookups correct
    import random as _r
    for first_char, tx, amt in _r.sample(survivors, min(10, len(survivors))):
        got = book[tx]
        assert got == amt, "Survivor amount mismatch"
    print("Survivor lookups OK ✅")