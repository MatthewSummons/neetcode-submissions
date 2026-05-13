class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Gather elements in a set for quick lookup
        num_set, seqs = {n for n in nums}, {}
        # Construct Sequences (if no succ, then seq_start)
        for n in nums:
            if n - 1 not in num_set:
                seqs[n] = None
        # Count length of each sequence
        for start in seqs.keys():
            seq_x, seq_len = start + 1, 1
            while seq_x in num_set:
                seq_len += 1
                seq_x += 1
            seqs[start] = seq_len
        if seqs:
            return max(seqs.values())
        else:
            return 0
        