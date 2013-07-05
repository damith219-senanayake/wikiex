'''
Created on Jul 6, 2013

@author: dracus
'''
#!/usr/bin/python

import MySQLdb

db= MySQLdb.connect("localhost","root","123","wikiex" )

cursor=db.cursor()

cursor.execute("select * from implication");

results=cursor.fetchall()
res2= results
count=0;
rw1=['a','a','a']
triplets=[]
triplets.append(rw1)
for row in results:
    ante = row[1]
    conse = row[2]
    print "%s ==> %s" % \
    (ante, conse )
    for ro in res2:
        ant2 = ro[1]
        if (ant2==conse):
            rw1=[ante,conse,ro[2]]
            print "%s ==> %s ==> %s" % \
            (ante, conse, ro[2])
        
        
            
    