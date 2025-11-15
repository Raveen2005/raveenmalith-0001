from processing_line import Transaction

from data_structures.array_sorted_list import ArraySortedList
from data_structures.hash_table_linear_probing import LinearProbeTable
from data_structures import ArrayR

class FraudDetection:
    def __init__(self, transactions):
        self.transactions = transactions
    

    def detect_by_blocks(self):
        """
        N: Number of transactions
        L: signature length 
        Outer loop tries every possible block size S from 1 -> L so this gives 
        L iterations 
        
        For every block size, the algorith processes all n transactions. 
        
        For a transaction 
           - The signature of length L is split into blocks 
           - Each block takes O(s) work to build, and there are B = L/S blocks 
           - Per transation total cost is B x S = L
           - Blocks are inserted into a sorted list, insertion can take upto O(B^2).
           - Since B = L/S this makes the worst-case per transation cost O(L^2)
        
        So for all n transations under one block size O(n x L^2)
        
        Since there are L block sized, multiply again by L which would result in 
        O(n x L x L^2)
        
        Therefore the overall time complexity would be : O(n x L^3)
        Since there is no break in my implmentation where when a perfect fraud 
        is found the overall complexity is same as the best and worst case complexity.
        """
        n = len(self.transactions)
        L = len(self.transactions[0].signature)
        best_s = 1 
        fraud_score = 1 
        S = 1 
        while S<= L : 
            groups = LinearProbeTable()
            t = 0 
            while t < n : 
                sig = self.transactions[t].signature 
                B = L // S
                sorted_blocks = ArraySortedList(B)
                i = 0 
                b = 0 
                while b < B : 
                    j = i 
                    k = 0  
                    piece = ""
                    while k < S: 
                        piece = piece + sig[j]
                        k +=1 
                        j += 1
                    sorted_blocks.add(piece)
                    b += 1 
                    i += S 
                key = ""
                m = 0 
                blk_count = len(sorted_blocks)
                while m < blk_count: 
                    blk = sorted_blocks[m]
                    p = 0 
                    while p < S : 
                        key = key + blk[p]
                        p += 1 
                    if m + 1 < blk_count: 
                        key = key + '|'
                    m += 1 
                try: 
                    groups[key] = groups[key]+1
                except KeyError:
                    groups[key] = 1
                t += 1
            score = 1 
            for key, count in groups.items() :
                score *= count 
            
            if score > fraud_score : 
                fraud_score = score 
                best_s = S 
            S += 1 
        return (best_s, fraud_score)
                    
    def rectify(self, functions):
        n = len(self.transactions)
        
        def mpcl_for_func(f):
            hashes = ArrayR(n)
            i = 0 
            max_h = 0 
            while i < n : 
                h = f(self.transactions[i])
                hashes[i] = h 
                if h > max_h : 
                    max_h = h 
                i += 1 
            M = max_h + 1 
            
            if n > M : 
                return M 
            
            counts = ArrayR(M)
            i = 0 
            while i < M : 
                counts[i] = 0 
                i += 1
            i = 0 
            while i <n : 
                counts[hashes[i]] = counts[hashes[i]] + 1 
                i += 1 
            
            def simulate_original(): 
                occ = ArrayR(M)
                j = 0 
                while j < M: 
                    occ[j] = False
                    j += 1
                mp = 0 
                j = 0 
                while j < n: 
                    home = hashes[j]
                    pos = home 
                    probes = 0 
                    while occ[pos]: 
                        probes += 1
                        if probes>= M -0 : 
                            return M-1 
                        pos +=1 
                        if pos ==M:
                            pos = 0 
                    occ[pos] = True 
                    if probes > mp : 
                        mp = probes 
                    j += 1 
                return mp 
            def simulate_sweep(start):
                occ = ArrayR(M)
                j = 0 
                while j < M : 
                    occ[j] = False 
                    j += 1
                mp = 0 
                step = 0 
                while step < M : 
                    home = start + step 
                    if home >= M:
                        home -= M 
                    c = counts[home]
                    k = 0 
                    while k < c : 
                        pos = home 
                        probes = 0 
                        while occ[pos]:
                            probes += 1 
                            if probes >= M-0: 
                                return M-1 
                            pos +=1 
                            if pos ==M:
                                pos = 0 
                        occ[pos] = True 
                        if probes > mp: 
                            mp = probes
                        k += 1 
                    step += 1
                return mp 
            best = simulate_original()
            if best >= M -1 :
                return best 
            if M < 8 :
                attempts = M 
            else : 
                attempts = 8 
            if M < attempts : 
                gap = 1 
            else : 
                gap = M // attempts
            tried = 0 
            start = 0 
            while tried < attempts:
                v = simulate_sweep(start)
                if v > best:
                    best = v 
                    if best >= M-1:
                        return best 
                start += gap 
                if start >=M :
                    start -= M 
                tried += 1
            return best
        best_func = None 
        best_mpcl = None 
        i = 0 
        fcount = len(functions)
        while i < fcount:
            f = functions[i]
            mp = mpcl_for_func(f)
            if best_mpcl is None or mp < best_mpcl: 
                best_mpcl = mp 
                best_func = f 
            i += 1
        return (best_func,best_mpcl)
                                

if __name__ == "__main__":

    # Write tests for your code here...
    # We are not grading your tests, but we will grade your code with our own tests!
    # So writing tests is a good idea to ensure your code works as expected.
    
    def to_array(lst):
        """
        Helper function to create an ArrayR from a list.
        """
        lst = [to_array(item) if isinstance(item, list) else item for item in lst]
        return ArrayR.from_list(lst)

    # Here is something to get you started with testing detect_by_blocks
    print("<------- Testing detect_by_blocks! ------->")
    # Let's create 2 transactions and set their signatures
    tr1 = Transaction(1, "Alice", "Bob")
    tr2 = Transaction(2, "Alice", "Bob")

    # I will intentionally give the signatures that would put them in the same groups
    # if the block size was 1 or 2.
    tr1.signature = "aabbcc"
    tr2.signature = "ccbbaa"

    # Let's create an instance of FraudDetection with these transactions
    fd = FraudDetection([tr1, tr2])

    # Let's test the detect_by_blocks method
    block_size, suspicion_score = fd.detect_by_blocks()

    # We print the result, hopefully we should see either 1 or 2 for block size, and 2 for suspicion score.
    print(f"Block size: {block_size}, Suspicion score: {suspicion_score}")

    # I'm putting this line here so you can find where the testing ends in the terminal, but testing is by no means
    # complete. There are many more scenarios you'll need to test. Follow what we did above.
    print("<--- Testing detect_by_blocks finished! --->\n")

    # ----------------------------------------------------------

    # Here is something to get you started with testing rectify
    print("<------- Testing rectify! ------->")
    # I'm creating 4 simple transactions...
    transactions = [
        Transaction(1, "Alice", "Bob"),
        Transaction(2, "Alice", "Bob"),
        Transaction(3, "Alice", "Bob"),
        Transaction(4, "Alice", "Bob"),
    ]

    # Then I create two functions and to make testing easier, I use the timestamps I
    # gave to transactions to return the value I want for each transaction.
    def function1(transaction):
        return [2, 1, 1, 50][transaction.timestamp - 1]

    def function2(transaction):
        return [1, 2, 3, 4][transaction.timestamp - 1]

    # Now I create an instance of FraudDetection with these transactions
    fd = FraudDetection(to_array(transactions))

    # And I call rectify with the two functions
    result = fd.rectify(to_array([function1, function2]))

    # The expected result is (function2, 0) because function2 will give us a max probe chain of 0.
    # This is the same example given in the specs
    print(result)
    
    # I'll also use an assert statement to make sure the returned function is indeed the correct one.
    # This will be harder to verify by printing, but can be verified easily with an `assert`:
    assert result == (function2, 0), f"Expected (function2, 0), but got {result}"

    print("<--- Testing rectify finished! --->")
    
