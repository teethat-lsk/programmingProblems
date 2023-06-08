function findMedianSortedArrays(nums1: number[], nums2: number[]): number {
  const combinded_list = nums1.concat(nums2)
  const findMedian = (array: number[]) => {
    if (array.length % 2 == 0) {
      const lowwer = (array.length / 2)-1;
      const upper = (array.length / 2);
      return (array[lowwer] + array[upper]) / 2;
    }
    return array[Math.floor(array.length / 2)];
  };

  //! Counting sort with Map()
  const countingSortWithMap = (nums1: number[], nums2: number[]) => {
    const combinded_list: number[] = nums1.concat(nums2);
    const counting_map = new Map<number, number>();
    const result_list: number[] = Array<number>(
      nums1.length + nums2.length
    ).fill(-9999999);
    const offset = Math.pow(10, 6);
    // const offset = 0
    combinded_list.forEach((num) => {
      if (counting_map.has(num + offset)) {
        let current_count: number = counting_map.get(num + offset) as number;
        counting_map.set(num + offset, current_count + 1);
      } else {
        counting_map.set(num + offset, 1);
      }
    });

    let counting_keys = [];
    for (let key of counting_map) {
      counting_keys.push(key[0]);
    }

    for (let i = 0; i < Math.max(...counting_keys); i++) {
      let current_count = counting_map.get(i);
      let next_count = counting_map.get(i + 1);
      if (current_count !== undefined) {
        if (next_count !== undefined) {
          counting_map.set(i + 1, current_count + next_count);
        } else {
          counting_map.set(i + 1, current_count);
        }
      }
    }

    console.log('combined', combinded_list);
    console.log('counting', counting_map);
    combinded_list.forEach((num) => {
      let index: number = counting_map.get(num + offset) as number;
      console.log(`assign ${num} at ${index}`);
      result_list[index] = num;
      counting_map.set(num + offset, index - 1);
    });
    const array = result_list.filter((num) => num !== -9999999);
    console.log(array);

    return findMedian(array);
  };

  //! Quick sort
  const quickSort = (
    array: number[],
  ): number[] => {
    if(array.length <=1){
      return array
    }
    const pivot = array[0]
    const left = []
    const right = []
    for (let i = 1; i < array.length; i++) {
      if (array[i] < pivot){
        left.push(array[i])
      }
      else{
        right.push(array[i])
      }
    }
    let result = quickSort(left).concat(pivot,quickSort(right)) 
    console.log(result)
    return result
}
return findMedian(quickSort(combinded_list))
}

console.log(findMedianSortedArrays([1, 3, 5, 1],[2, 4, 6, 7]));
