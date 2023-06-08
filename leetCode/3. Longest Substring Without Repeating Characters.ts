// ACBDGD length = 6
// len = 5 ACBDG CBDGD
// len = 3 ACB CBD BDG DGB

// Brute force shit
// function lengthOfLongestSubstring(s: string): number {
//   const regex: RegExp = /(.).*\1/;
//   const string1: string = 'abcabcb';

//   const string2: string = 'world';

//   for(let len=s.length;len>=0;len--){
//     for(let start=0;start+len<=s.length;start++){
//         let subString = s.slice(start, start + len );

//         if(!regex.test(subString)){
//             return len
//         }
//     }
//   }

//   return 0;
// }

function lengthOfLongestSubstring(s: string): number {
  const window: string[] = [];
  let longest = 0;

  for (const char of s) {
    const possibleIndex = window.indexOf(char);

    if (possibleIndex !== -1) {
      window.splice(0, possibleIndex + 1);
    }
    window.push(char);
    longest = Math.max(longest, window.length);
  }

  return longest;
}




