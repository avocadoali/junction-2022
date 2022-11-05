# Junction 2022 - Nexi Challenge - Crack the Payments
### Project by: 2 Coders 1 Card

## The Result
We managed to access the cards internal filesystem, read it and interpret most of its contents. As demonstration we wrote a tool, which allows you to read any Visa or Master card through a smartcard reader and display selected contents of the card. We show the user the most interesting pieces of information and give a brief explanation why it is potentially harmful information.

Here are some examples of what we managed to retrieve from the cards smartchip:
-	Name of the card Holder
-	Card Number
-	Expiration Date
-	Country and Currency
-	Payment log (Amounts and Dates)

The first pieces of information are especially critical. To understand why one has to look at how online payment with credit cards work: You have to enter the card number, name of the holder, expiration date and CVV to verify that you physically are in possession of the card. So the only missing piece to successfully do payments are the three digits of the CVV number. In contrast to the card PIN where the user has only 3 tries to authenticate himself at a payment terminal, the CVV does not have limited guesses. In fact, in 2017 researchers from the Newcastle University proposed a distributed guessing attack to brute force this number while distributing the guesses over many different web shops, to fly under the radar. 

The second interesting part are the payment logs. In our examples we found that the card stores the 10 most recent payments. You can read amount and the date of the payments. This is less a security issue but more a privacy concern. Payment data is highly sensitive information and no one except yourself should be able to access it.  This means that theoretically every time you use your card, someone could access your payment history.

## The Process

#### 1.	Communication with the card
-	As a starting point we had to learn about the smartcard command pattern, file system and responses.
-	The two commands we had to use the most are 0x00A40400[APP] which selects a specific Application Folder on the card and "0x00B2[Record][File]" which is used to retrieve all of the contents of the selected Application

#### 2.	Reading the complete file system and understanding its content
-	With these commands we were able to read out the whole card.
-	The exciting part was interpreting the read contents. It was like digging for gold. It is to note that none of the data we interpreted was encrypted and it did not take significantly more effort to read than a simple ascii conversion or ISO-Code lookup.
-	We filtered through the found data and identified potentially harmful information to focus on for our presentation.

#### 3.	Creating The Challenge Demo
-	We used a python backend to communicate with the smartcard via the reader and setup a flask boostrap for the frontend.
-	Our goal was to read a card and visualize the found juicy information. The user has the possibility to read further into the findings and understand their possible impact 
-	We also visualize the real communication log between the card and backend and show the corresponding human readable awnsers.


## Further thoughts
Application of the findings:
For our demo we used a smartcard reader to communicate with the card. This means we had to create a physical connection between card and reader. This makes the vulnerability which is created by reading the card number, expiration date and holder less severe, because all of this information is actually physically written on the card. 
This said: all of the modern payment cards support communication via NFC, so indeed contactless communication. This could be done for example by holding a reader close to a wallet or a sealed envelope. Communication between card and reader is still done following the same protocols and with the same approach as ours the similar information can be retrieved, resulting in a realistic attack scenerio!

We think payment data is highly sensetive data and should never be transmitted without a form of encryption. Encryption would make the theft of credit card data much more difficult and therefore more unlikely.  
Concerning the backlog of the transaction history the same holds, it is irresponsible to keep them lying around unencrypted. We are not sure why they are even stored at all, because each payment terminal will communicate with the banking network anyways but if they are necessary, at least keep them encrypted!

