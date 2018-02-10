import sys
import heapq

def percentile(arr,p):
    n  = len(arr)
    #arr = sorted(arr)
    if (p *n)%100 == 0:
        return arr[int((float(p)/100)*n) -1]
    else:    
        return arr[int((float(p)/100)*n) ]

def getValues(line):
    
    try:
        all_values = line.split("|")
                
        recipient = all_values[0]
        donor_name = all_values[7]
        zip_code = int(all_values[10][:5])
        year = int(all_values[13][-4:])
        amt = int(all_values[14])
        other_id = all_values[15]    
        
        if recipient != '' and donor_name != '' and amt > 0 and other_id   == '':
            return [recipient, donor_name, zip_code, year, amt]
        else:
            return None
        
    except:
        return None

if __name__ == "__main__":

    filename = sys.argv[1]
    f = open(filename)
    data = f.readlines()    
    repeatedDonor = {} # repeat donor
    recipientRecord = {} # repeated transaction
    
    f2 = open(sys.argv[2])
    
    try:
        p = int(f2.read())
    except:
        print "percentile reading error..terminating"
        sys.exit()
    
    output_file = open(sys.argv[3],"w")
    
    for line in data:
                
        vals = getValues(line)

        if(vals):
            recipient, donor_name, zip_code, year, amt = vals
        else:
            print "Skipping", line
            continue
                    
        name_and_zip = donor_name+"|"+str(zip_code)
            
        if name_and_zip in repeatedDonor: #Its a repeated donor
                                                    
             # add the current record for the repeated donor
                
            recipient_zip_year = recipient+"|"+ str(zip_code)+"|"+str(year)
                
            if recipient_zip_year in recipientRecord:

                heap, sum_amt, cnt = recipientRecord[recipient_zip_year]

                heapq.heappush(heap, amt)
                cnt += 1
                sum_amt += amt
                recipientRecord[recipient_zip_year] = [heap,sum_amt,cnt ]
            else:
                heap = [amt]
                cnt = 1
                sum_amt = amt
                recipientRecord[recipient_zip_year] = [heap,sum_amt,cnt ]                                                               
            
            recipient1 , zip_code1, year1 , amt1, seen = repeatedDonor[name_and_zip].split("|")
	    # find the first record of this donor

            if seen == "False": # first record has not been seen, add the first record
                                    
                 recipient_zip_year1 = recipient1+"|"+zip_code1+"|"+year1 #make the key for the first record
                
                 if recipient_zip_year1 in recipientRecord:   # check if this key already exists in the transactions
                     heap, sum_amt, cnt = recipientRecord[recipient_zip_year1]
                     heapq.heappush(heap, int(amt1))
                     cnt += 1
                     sum_amt += int(amt1)
                     recipientRecord[recipient_zip_year1] = [heap,sum_amt,cnt] #append the first record value
                 else:
                     heap = [int(amt1)]
                     cnt = 1
                     sum_amt = int(amt1)
                     recipientRecord[recipient_zip_year1] = [heap,sum_amt,cnt ] #make the first entry
                        
                 repeatedDonor[name_and_zip] = recipient_zip_year1+"|"+amt1+"|"+"True" #change the value to be seen 
                
            heap,sum_amt,cnt = recipientRecord[recipient_zip_year]
                
            percentile_p = str(percentile(heap,p))
                
            output = recipient_zip_year+"|"+percentile_p+"|"+str(sum_amt)+"|"+str(cnt)+"\n"
            output_file.write(output)
                #print output
                
        else:
                
            repeatedDonor[name_and_zip] = recipient +"|"+ str(zip_code) +"|"+ str(year) +"|"+ str(amt) +"|"+"False" #has not been seen
                

output_file.close()                    
