import sqlite3
sqlite_file = 'url_storage_dist.sqlite'
conn = sqlite3.connect(sqlite_file)
c = conn.cursor()




totalTables = 0
totalColumns = 0
totalRows = 0
totalCells = 0

# Get List of Tables:      
tableListQuery = "SELECT name FROM sqlite_master WHERE type='table' ORDER BY Name"
c.execute(tableListQuery)
tables = map(lambda t: t[0], c.fetchall())

for table in tables:
           
        
    columnsQuery = "PRAGMA table_info(%s)" % table
    c.execute(columnsQuery)
    numberOfColumns = len(c.fetchall())
    
    rowsQuery = "SELECT Count() FROM %s" % table
    c.execute(rowsQuery)
    numberOfRows = c.fetchone()[0]
    
    numberOfCells = numberOfColumns*numberOfRows
    
    print("%s\t%d\t%d\t%d" % (table, numberOfColumns, numberOfRows, numberOfCells))
    
    totalTables += 1
    totalColumns += numberOfColumns
    totalRows += numberOfRows
    totalCells += numberOfCells


# Select only url column, 10 rows
c.execute('SELECT url FROM {tn} LIMIT 10'.\
        format(tn='metadata'))
ten_rows = c.fetchall()
for link in ten_rows:
    print link[0]
    

    

    