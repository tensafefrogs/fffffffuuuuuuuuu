#!/usr/bin/python

import urllib2
import json

f_count = 3;
u_count = 3;
f = 'f'
u = 'u'

url_template = 'http://ajax.googleapis.com/ajax/services/search/web?v=1.0&q=%s'

full_result =[] 

for x in range(1, f_count + 1):
  for y in range(1, u_count + 1):
    query = (f * x) + (u * y)
    url = url_template % query 

    req = urllib2.Request(url)
    req.add_header('Referer', 'http://blog.deconcept.com/')
    data = urllib2.urlopen(req)
    print 'requesting url %s' % url

    result = data.read()

    parsed_result = json.loads(result)
    print parsed_result['responseData']['cursor']['estimatedResultCount']

    full_result.append({
      'query': query,
      'count': int(parsed_result['responseData']['cursor']['estimatedResultCount']),
      'f': x,
      'u': y
    })

# After we get all the results, go through and set a % value,
# where 100% is the max count, and 0% is the lowest count.
max_value = 0.0
min_value = full_result[0]['count']

for x in range(len(full_result)):
  current_count = full_result[x]['count']
  if max_value < current_count:
    max_value = float(current_count)
  if min_value > current_count:
    min_value = current_count

print 'max value is %s' % max_value
print 'min value is %s' % min_value

for x in range(len(full_result)):
  current_item = full_result[x]
  print current_item['count']
  current_item['percent'] = int((current_item['count'] / max_value) * 100.0)


print json.dumps(full_result, sort_keys=True, indent=4)






