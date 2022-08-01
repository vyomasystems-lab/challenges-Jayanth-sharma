# challenges-Jayanth-sharma
challenges-Jayanth-sharma created by GitHub Classroom
# Results:
## level-1 
### Design-1 Bug Capture:
![image](https://user-images.githubusercontent.com/53760504/181523667-a8a8ead6-5c42-4dd5-bd44-88b1f37875e9.png)
### Design-1 Debug:<br/>
  the bug occured due to absents of ` 5'b11110: out = inp30; ` .<br/>
![image](https://user-images.githubusercontent.com/53760504/181551350-c8fda7c1-f96d-43c0-a3d3-a061a704934b.png)
### Design-2 Bug Capture:<br/>
   The Bug Failed to In design of Overlapping Condition.<br/>
   ![image](https://user-images.githubusercontent.com/53760504/182183317-e28bd979-9438-494a-8e5a-34462064a6e0.png)
### Design-2 Debug:
   Here Form Line 60 to line 70: The Code ends Return to IDLE state instead of verification for overlap. <br/>
   Considering a Meanly Machine the FSM for Sequence Detector for Overlaping 1011 sequence: <br/>
   
   ![kwmgI](https://user-images.githubusercontent.com/53760504/182186550-0f4a599a-6a58-427d-8af4-a9fd5d149eb2.png)
   
   ```
    SEQ_101:
      begin
        if(inp_bit == 1)
          next_state = SEQ_1011;
        else
          next_state = SEQ_101;
      end
      SEQ_1011:
      begin
        next_state = SEQ_10 ;
      end
   
   ```
   
  
