class Solution:
	def lengthOfLongestSubstring(self, string):
		chars = list(string)
		stack = ""
		curr = ""
		max_count = 0
		
		for i in chars:
			if chars.index(i) != len(chars) - 1:
				if i == chars[chars.index(i)+1]:
					curr += i
					print(curr)
				else:
					if len(curr) > max_count:
						stack = curr
					curr = ""
				#print(stack, curr)

Solution().lengthOfLongestSubstring("asdsbbbsdbcccsahh")