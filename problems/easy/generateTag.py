
import re
class Solution(object):
    def generateTag(self, caption: str) -> str:
        """
        Generate a hashtag from the given caption.
        
        :type caption: str
        :rtype: str
        """
        words = re.findall(r'[a-zA-Z]+', caption)
        if not words:
            return "#"

        tag = words[0].lower() + ''.join(word.capitalize() for word in words[1:])

        tag = '#' + tag

        return tag[:100]