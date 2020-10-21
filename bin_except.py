# Author: Quanyue Xie
# Date: 10/21/2020
# Description： include a TargetNotfound class, once the target
#is not in the list, in will be triggered. It also can tell you
#the location of the target in a list

class TargetNotFound(Exception):
    def __init__(self, message):
        # Call the base class constructor with the parameters it needs
        super().__init__(message)


def binary_search(a_list, target):
  """
  Searches a_list for an occurrence of target
  If found, returns the index of its position in the list
  If not found, returns -1, indicating the target value isn't in the list
  """
  first = 0
  last = len(a_list) - 1
  while first <= last:
    middle = (first + last) // 2
    if a_list[middle] == target:
      return middle
    if a_list[middle] > target:
      last = middle - 1
    else:
      first = middle + 1
  raise TargetNotFound("the target value isn't in the list")


if __name__ == "__main__":
    a_list = [1,2,3,4,5,6,7,8,9,10]
    #you can use 11 to trigger Target not found
    target = 6
    result = binary_search(a_list, target)
    print("the location is in {}".format(result))


