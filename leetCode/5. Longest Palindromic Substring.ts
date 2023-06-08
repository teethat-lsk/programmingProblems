function longestPalindrome(s: string): string {
  let currentStr = '',
    maxStr = '';

  for (let i = 0; i < s.length; i++) {
    let oddString = expand(s, i, i);
    let evenString = expand(s, i, i + 1);
    currentStr = oddString.length > evenString.length ? oddString : evenString;
    maxStr = maxStr.length > currentStr.length ? maxStr : currentStr;
  }
  return maxStr;
}

function expand(s: string, left: number, right: number): string {
  while (left >= 0 && right <= s.length && s[left] === s[right]) {
    left -= 1; // make left go outwards;
    right += 1; // make right go outwards;
  }
  return s.substring(left + 1, right); // same principal as including right, but using the left pointer
}
