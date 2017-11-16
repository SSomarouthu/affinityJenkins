# No need to process files and manipulate strings - we will
# pass in lists (of equal length) that correspond to
# sites views. The first list is the site visited, the second is
# the user who visited the site.

# See the test cases for more details.

def highest_affinity(site_list, user_list, time_list):
  # Returned string pair should be ordered by dictionary order
  # I.e., if the highest affinity pair is "foo" and "bar"
  # return ("bar", "foo").

  from collections import defaultdict
  my_dict = defaultdict(list)
  for k, v in zip(user_list, site_list):
      my_dict[k].append(v)
  print("my_dict is: ", my_dict)
  
  # i=1
  # if(i==1):
	# i=1;
  # else:
	# i=1;
	# i=1;
	# i=1;
	# i=1;
	# i=1;
	# i=1;
	# i=1;
	# i=1;
	# i=1;
	# i=1;
	# i=1;
	# i=1;
	# i=1;
	# i=1;
	# i=1;
	# i=1;
	# i=1;
	# i=1;
	# i=1;
	# i=1;
	# i=1;
	# i=1;
	# i=1;
	# i=1;
	# i=1;
	# i=1;
	# i=1;
	# i=1;
	# i=1;
	# i=1;
	# i=1;
	# i=1;
	# i=1;
	# i=1;
	# i=1;
	# i=1;
	# i=1;
	# i=1;
	# i=1;
	# i=1;
	# i=1;
	# i=1;
	# i=1;
	# i=1;
	# i=1;
	# i=1;
	# i=1;
	# i=1;
	# i=1;
	# i=1;
	# i=1;
	# i=1;
	# i=1;
	# i=1;
	# i=1;
	# i=1;
	# i=1;
	# i=1;
	# i=1;
	# i=1;
	# i=1;
	# i=1;
	# i=1;
	# i=1;
	# i=1;
	# i=1;
	# i=1;
	# i=1;
	# i=1;


  mystr = site_list
  mydict = {}
  new_dict = {}
  lm_dict = {}
  maxfreq_dict = {}
  site_dict = {}
  # get the unique characters
  unique_chars = sorted(set(mystr), key=mystr.index)
  # store the characters and their respective frequencies in the dictionary
  for c in unique_chars:
      ctr = 0
      for d in mystr:
          if d != " " and d == c:
              ctr = ctr + 1
      mydict[c] = ctr
  # print(mydict)
  # store the maximum frequency
  max_freq = max(mydict.values())
  print("the highest frequency of occurence: ", max_freq)

  print("the sites are:")

  for k, v in mydict.items():
      if v == max_freq:
          print("k is: ", k)
          for i in my_dict:
              if (k in my_dict[i]):
                  print("i is: ", i)
                  new_dict[i] = my_dict[i]
          flat_list = [item for sublist in new_dict.values() for item in sublist]
          lm_dict[k] = flat_list
          flat_list[:] = [x for x in flat_list if x != k]
          print("filtered list is: ", flat_list)
          mystr1 = flat_list
          mydict1 = {}

          # get the unique characters
          unique_chars1 = sorted(set(mystr1), key=mystr1.index)
          # store the characters and their respective frequencies in the dictionary
          for c1 in unique_chars1:
              ctr1 = 0
              for d1 in mystr1:
                  if d1 != " " and d1 == c1:
                      ctr1 = ctr1 + 1
              mydict1[c1] = ctr1
          # print(mydict)
          # store the maximum frequency
          max_freq1 = max(mydict1.values())
          maxfreq_dict[k] = max_freq1
          print("the highest frequency of occurence: ", max_freq1)

          print("the sites are:")
          for k1, v1 in mydict1.items():
              if v1 == max_freq1:
                  print("k1 is: ", k1)
                  site_dict[k] = k1  # need to modify for multiple sites

  print(lm_dict)
  print(maxfreq_dict)
  print(site_dict)
  print("max is:", max(maxfreq_dict.values()))
  
  for x, y in maxfreq_dict.items():
      if y == (max(maxfreq_dict.values())):
          print("x is :", x)
          print(site_dict[x])
  new1 = (site_dict[x],x)
  return (tuple(sorted(new1)))