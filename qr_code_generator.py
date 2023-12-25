#first of all we have to import qrcode module
import qrcode

#use make function to create image of Qr code you can provide any link or message to the QR Code
image = qrcode.make("Congratulation your QR is created Successfully")

#After creating image we have to save the image using save function it will get saved in your python folder
image.save("qrcode1.png")
