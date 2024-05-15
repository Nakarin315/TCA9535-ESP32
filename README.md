The TCA9535 is a 16-bit I/O expander used to trigger digital pins to be HIGH or LOW.  Here, we use the ESP32-WROOM-32 to communicate with the TCA9535 via IO21 (SDA) and IO22 (SCL) as shown below, using the I2C (two-wire serial communication) protocol.
We need to use Thonny to compile 

1) Plug the ESP32 into the computer
2) Open Thonny and change the interpreter to MicroPython ESP32 this will show up only when the board has connected to your computer
   
![image](https://github.com/Nakarin315/TCA9535_ESP32/assets/93529299/5150bc3e-4aa1-4b62-ba27-c6b15b601406)


This code is basically pulse pins P00- P07 to HIGH for 200ms and LOW for 100ms while P08- P17 are pulse oppositely and the result are show below so the code work as we expected
![image](https://github.com/Nakarin315/TCA9535_ESP32/assets/93529299/00791a69-238a-4261-a873-0e22f69e0ea2)
![image](https://github.com/Nakarin315/TCA9535_ESP32/assets/93529299/485692f7-215d-4106-bf06-fa3b146f76fa)

