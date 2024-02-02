# Nama  :   Ilham Ghani Adrin Sapta
# NPM   :   2306201792

import turtle

jarak = 1                                           # menginisialisasi program dengan meminta semua input integer dengan batasan sesuai yang diberikan
perbedaan_layer = 1
jumlah_tower = int(turtle.numinput('Towers to Build', 'Enter the amount of tower you want to build (min 1)', minval=1))
if jumlah_tower > 1:                                # membuat pengecualian saat jumlah tower hanya 1 maka program tidak akan meminta jarak dan perbedaan layer
    jarak = int(turtle.numinput('Distance between Towers', 'Enter the distances between each towers (min 2, max 5)', minval=2, maxval=5))
    perbedaan_layer = int(turtle.numinput('Difference in Layers', 'Enter the layer difference between each towers (min 2, max 5)', minval=2, maxval=5))
panjang_bata = int(turtle.numinput('Brick length', 'Enter each brick length (max 35)', minval=1, maxval=35))
lebar_bata = int(turtle.numinput('Brick width', 'Enter each brick width (max 25)', minval=1, maxval=25))
layer_tower_pertama = int(turtle.numinput('First Tower Length', 'Enter the amount of layer for the first tower (max 25)',minval=1, maxval=25))
panjang_layer = int(turtle.numinput('Layer length', 'Enter how many bricks in each layer (max 10)',minval=1, maxval=10))
counter = 0                                          # menginisialisasi counter untuk menghitung jumlah bata

gan = turtle.Turtle()
gan.up()
gan.setposition((((panjang_bata * panjang_layer * jumlah_tower + jarak * panjang_bata * jumlah_tower) / 2) + jarak * panjang_bata) * (-1), 0)     
# ini untuk memindahkan turtle agar keseluruhan tower berada ditengah 
gan.speed(0)

for i in range(jumlah_tower):                       # for loop untuk keseluruhan tower
    gan.setposition(gan.xcor() + jarak * panjang_bata, -200)
    current_layer_tower = layer_tower_pertama + i * perbedaan_layer  # menginisiasi variabel baru agar tinggi setiap badan tower terus bertambah sesuai input perbedaan layer  
    gan.pendown()   
    for i in range(current_layer_tower):            # for loop untuk setiap layer di bodi tower
        for i in range(panjang_layer):              # for loop untuk 1 layer
            gan.color("maroon", "#CA7F65")
            gan.pendown()
            gan.begin_fill()
            for i in range(2):                      # for loop untuk 1 bata
                gan.forward(panjang_bata)
                gan.left(90)
                gan.forward(lebar_bata)
                gan.left(90)
            gan.end_fill()
            gan.penup()
            gan.forward(panjang_bata)
        
        gan.backward(panjang_bata * panjang_layer)  # turtle akan memposisikan diri agar bisa membangun bagian atas tower tepat ditengah badan tower
        gan.left(90)
        gan.forward(lebar_bata)
        gan.right(90)
        counter += panjang_layer                    # counter akan bertambah sebanyak panjang layer dan akan terus mengulang hingga loop current_layer berakhir
    gan.backward(panjang_bata / 2)          

    for i in range(panjang_layer + 1):              # for loop untuk bagian atas tower
        gan.color("maroon", "#693424")
        gan.pendown()
        gan.begin_fill()
        for i in range(2):                          # for loop untuk satu bata
            gan.forward(panjang_bata)
            gan.left(90)
            gan.forward(lebar_bata)
            gan.left(90)  
        gan.forward(panjang_bata)
        gan.end_fill()
    gan.left(90)
    gan.forward(lebar_bata)
    gan.right(90)
    gan.backward((panjang_bata / 2) + ((panjang_layer + 1) * panjang_bata // 2))
    gan.color("black", "#FFE4C4")
    gan.begin_fill()                                # for loop untuk badan jamur
    for i in range(5):
        gan.forward(panjang_bata)
        gan.left(90)
    gan.end_fill()
    gan.color("black", "red")
    gan.forward(panjang_bata)
    gan.right(90)
    gan.forward(panjang_bata/2)
    gan.begin_fill()
    gan.left(90)
    gan.circle(panjang_bata, 180)                   # setengah lingkaran untuk bagian atas jamur
    gan.left(90)
    gan.forward(panjang_bata/ 2)
    gan.end_fill()
    gan.penup()
    gan.forward((panjang_layer / 2 + 1) * panjang_bata)
    counter += panjang_layer + 1                    # counter bertambah sebanyak bata di atap tower

gan.up()
gan.goto(0, -300)                                   # program berakhir dengan menampilkan informasi tower dan jumlah bata dibagian tengah bawah layar
gan.write(f"{jumlah_tower} Super Mario towers has been built with a total of {counter} Bricks", align="center", font=("Arial", 16, "normal"))
gan.hideturtle()
turtle.done()


#kolaborator:       Imam Fajri          NPM =  2306165566
#                   Bryan Mitch         NPM =  2306165742
                