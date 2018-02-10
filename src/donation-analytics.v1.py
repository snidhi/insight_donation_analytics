import sys
import heapq

def percentile(arr,p):
    n  = len(arr)
    #arr = sorted(arr)
    if (p *n)%100 == 0:
        return arr[int((float(p)/100)*n) -1]
    else:    
        return arr[int((float(p)/100)*n) ]


if __name__ == "__main__":

    filename = sys.argv[1]
    f = open(filename)
    data = f.readlines()    
    repeatedDonor = {} # repeat donor
    resipientRecord = {} # repeated transaction
    
    f2 = open(sys.argv[2])
    
    p = int(f2.read())
    
    output_file = open(sys.argv[3],"w")
    
    for line in data:
        record = line.split('|')
        id = record[0]
        name = record[7]
        zip = record[10]
        date = record[13]
        amt = record[14]
        other_id = record[15]
        
        if id != '' and name != '' and zip != '' and len(zip) > 4 and date != '' and amt != 0 and other_id   == '':
            
            name_and_zip = name+"|"+zip[:5]
            
            if name_and_zip in repeatedDonor: #Its a repeated donor
                                                    
                # add the current record for the repeated donor
                
                resipient_zip_year = id+"|"+zip[:5]+"|"+date[-4:]
                
                if resipient_zip_year in resipientRecord:

                    heap, sum_amt, cnt = resipientRecord[resipient_zip_year]
                    #b.append(int(amt))
                    heapq.heappush(heap, int(amt))
                    cnt += 1
                    sum_amt += int(amt)
                    resipientRecord[resipient_zip_year] = [heap,sum_amt,cnt ]
                else:
                    heap = [int(amt)]
                    cnt = 1
                    sum_amt = int(amt)
                    resipientRecord[resipient_zip_year] = [heap,sum_amt,cnt ]               
                                                
                
                id1 , zip1, date1 , amt1, seen = repeatedDonor[name_and_zip].split("|") # find the first record of this donor

                if seen == "False": # first record has not been seen, add the first record
                                        
                     resipient_zip_year1 = id1+"|"+zip1[:5]+"|"+date1[-4:] #make the key for the first record
                    
                     if resipient_zip_year1 in resipientRecord:   # check if this key already exists in the transactions
                         heap, sum_amt, cnt = resipientRecord[resipient_zip_year1]
                         #b.append(int(amt1))
                         heapq.heappush(heap, int(amt1))
                         cnt += 1
                         sum_amt += int(amt1)
                         resipientRecord[resipient_zip_year1] = [heap,sum_amt,cnt] #append the first record value
                     else:
                         heap = [int(amt1)]
                         cnt = 1
                         sum_amt = int(amt1)
                         resipientRecord[resipient_zip_year1] = [heap,sum_amt,cnt ] #make the first entry
                        
                     repeatedDonor[name_and_zip] = id1 +"|"+zip1+"|"+date1+"|"+amt1+"|"+"True" #change the value to be seen 
                
                heap,sum_amt,cnt = resipientRecord[resipient_zip_year]
                
                percentile_p = str(percentile(heap,p))
                
                output = resipient_zip_year+"|"+percentile_p+"|"+str(sum_amt)+"|"+str(cnt)+"\n"
                output_file.write(output)
                #print output
                
            else:
                
                repeatedDonor[name_and_zip] = id +"|"+zip+"|"+date+"|"+amt+"|"+"False" #has not been seen
                

output_file.close()                    
