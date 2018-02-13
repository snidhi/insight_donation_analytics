# See READme for more details
import sys
import heapq


def percentile(heap,p,size):
    # percentile is normalized rank in sorted array (heap)
    if (p * size)%100 == 0:
        return heap[int((float(p)/100)*size) -1]
    else:    
        return heap[int((float(p)/100)*size)]

def getValues(line):
    
    try:
        all_values = line.split("|")
                
        recipient = all_values[0]
        donor_name = all_values[7]
        zip_code = all_values[10][:5]
	date = all_values[13]
        year = all_values[13][-4:]
	int(date)
	int(zip_code)
	int(year)
        amt = int(all_values[14])
        other_id = all_values[15]    
        
	if recipient != '' and len(date) == 8 and donor_name != '' and len(zip_code) > 4 and amt > 0 and other_id   == '':
            return [recipient, donor_name, zip_code, year, amt]
        else:
            return None
        
    except:
        return None
        
if __name__ == "__main__":

    from datetime import datetime
    startTime = datetime.now()

    try:
    	input_file = open(sys.argv[1])
    except:
	    print "Unable to open input file. Terminating!"
	    sys.exit()
    
    try:
    	percentile_file = open(sys.argv[2])
        p = int(percentile_file.read())
    except:
        print "Unable to open percentile file. Terminating!"
        sys.exit()
    finally:
	    if(percentile_file is not None):
		percentile_file.close()                    

    try: 
    	output_file = open(sys.argv[3],"w")
    except:
	print "Unable to open output file. Terminating!"
	sys.exit()

    #key = string : donor name + | + zip 
    #value = string : First contribution of this donor. Of that contribution: recipient id + zip + year + amt + True/False (processed or not)
    #maximum size of the hash map can go to as big as the number of unique donors
    repeatedDonor = {}
    
    #key = recipient id + zip + year 
    #value = heap of contributions, sum of contributions, # of contributions
    #maximum number of keys can go to as high as the number of lines in the input. 
    recipientRecord = {} 
    
    valid_lines = 0	
    skipped_lines = 0 
    
    line =  input_file.readline()
    while (line): 
        vals = getValues(line)
	line = input_file.readline()

        if(vals):
            recipient, donor_name, zip_code, year, amt = vals
	    valid_lines += 1
        else:
	    skipped_lines += 1 
            continue
                    
        name_and_zip = donor_name + "|" + zip_code # key for donor map
        recipient_zip_year = recipient + "|" + zip_code + "|" + year # key for recipient map

        donor_record = repeatedDonor.get(name_and_zip) 

        if (donor_record != None):
             #Its a repeat donor                                      
            
	    recipient_record = recipientRecord.get(recipient_zip_year)    
            if recipient_record != None:
                # Current recipient has recevied donations from this zip and year
                heap, sum_amt, cnt = recipient_record
                heapq.heappush(heap, amt)
                cnt += 1
                sum_amt += amt
            else: 
		# Current recipient is reciving donations for first time from this zip and year
                heap = [amt]
                cnt = 1
                sum_amt = amt

            
	    # We may not have processed first record of this repeat donor, so lets do that now.
            recipient1 , zip_code1, year1 , amt1, seen = donor_record.split("|")
            if seen == "False": 
                 recipient_zip_year1 = recipient1 + "|" + zip_code1 + "|" + year1 
		 if (recipient_zip_year1 == recipient_zip_year):
			 # recipient, zip and year corresponding to first record of current repeat donor
			 # is same as that of current line we are processing, so we need to account this for current line too.
			 heapq.heappush(heap, int(amt1))
			 cnt += 1
			 sum_amt += int(amt1)
		 else:	 
		 	# first record of current repeat donor is for different recipient, zip and year
			recipient_previous_record = recipientRecord.get(recipient_zip_year1)                
                 	if recipient_previous_record != None:   
				# this recipient, zip and year already exists, so add to its record
                     		heap1, sum_amt1, cnt1 = recipient_previous_record
                     		heapq.heappush(heap1, int(amt1))
                     		cnt1 += 1
                     		sum_amt1 += int(amt1)
                 	else:
				# this recipient, zip and year is seen for first time
                     		heap1 = [int(amt1)]
                     		cnt1 = 1
                     		sum_amt1 = int(amt1)

                        recipientRecord[recipient_zip_year1] = [heap1,sum_amt1,cnt1 ] #update recipient map for this donor's first entry
		 repeatedDonor[name_and_zip] = recipient_zip_year1+"|"+amt1+"|"+"True" #change the value to be seen now that its prcoessed 
        
		 # first record of current donor has not been processed 

            recipientRecord[recipient_zip_year] = [heap,sum_amt,cnt]                                                               
            percentile_p = str(percentile(heap,p,cnt))
            output = recipient_zip_year+"|"+percentile_p+"|"+str(sum_amt)+"|"+str(cnt)+"\n"
            output_file.write(output)
                
        else:
            # we are seeing this donor for first time   
            repeatedDonor[name_and_zip] = recipient +"|"+ str(zip_code) +"|"+ str(year) +"|"+ str(amt) +"|"+"False" 
                
    print "Finished in ",datetime.now() - startTime
    print skipped_lines, "lines are skipped due to malformed data or other_id is not empty"
    print valid_lines, "valid lines that are processed"
    output_file.close()                    
    input_file.close()                    

