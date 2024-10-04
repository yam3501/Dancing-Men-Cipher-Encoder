from PIL import Image
from os import system, path
from time import sleep
from string import ascii_lowercase

letters4 = list(ascii_lowercase)                                                # List of lowercase letters for indexing

men = [                                                                         # List of file paths for dancing men images corresponding to each letter
    "dancing_men_images/A.png", 
    "dancing_men_images/B.png", 
    "dancing_men_images/C.png", 
    "dancing_men_images/D.png", 
    "dancing_men_images/E.png", 
    "dancing_men_images/F.png", 
    "dancing_men_images/G.png", 
    "dancing_men_images/H.png", 
    "dancing_men_images/I.png", 
    "dancing_men_images/J.png", 
    "dancing_men_images/K.png", 
    "dancing_men_images/L.png", 
    "dancing_men_images/M.png", 
    "dancing_men_images/N.png", 
    "dancing_men_images/O.png", 
    "dancing_men_images/P.png", 
    "dancing_men_images/Q.png", 
    "dancing_men_images/R.png", 
    "dancing_men_images/S.png", 
    "dancing_men_images/T.png", 
    "dancing_men_images/U.png", 
    "dancing_men_images/V.png", 
    "dancing_men_images/W.png", 
    "dancing_men_images/X.png", 
    "dancing_men_images/Y.png", 
    "dancing_men_images/Z.png"
]

flag_men = [                                                                    # List of file paths for flag images (used for the last letter in a word)
    "flag_images/flag_a.png",     
    "flag_images/flag_b.png", 
    "flag_images/flag_c.png", 
    "flag_images/flag_d.png", 
    "flag_images/flag_e.png", 
    "flag_images/flag_f.png", 
    "flag_images/flag_g.png", 
    "flag_images/flag_h.png", 
    "flag_images/flag_i.png", 
    "flag_images/flag_j.png", 
    "flag_images/flag_k.png", 
    "flag_images/flag_l.png", 
    "flag_images/flag_m.png", 
    "flag_images/flag_n.png", 
    "flag_images/flag_o.png", 
    "flag_images/flag_p.png", 
    "flag_images/flag_q.png", 
    "flag_images/flag_r.png", 
    "flag_images/flag_s.png", 
    "flag_images/flag_t.png", 
    "flag_images/flag_u.png", 
    "flag_images/flag_v.png", 
    "flag_images/flag_w.png", 
    "flag_images/flag_x.png", 
    "flag_images/flag_y.png", 
    "flag_images/flag_z.png"
]

d = '0'                                                                         # Main loop for program options
while (d != '1') or (d != '2'):
    system("cls")
    print("################################")
    print("#  Dancing Men Cipher Encoder  #")
    print("################################\n")
    print("# Options: \n")
    print("1] Encode")
    print("2] Exit\n")

    d = input("Choose option: ")                                                # User input for selecting the option
    if d == '1':                                                                # Option to encode a message
        sleep(0.5)
        msgw = list(input("Enter message: ").split())                           # Input message to encode, split into words
        dancing_men_images = []
        count = 0
        for i in range(len(msgw)):                                              # Loop through each word in the message
            for j in msgw[i]:                                                   # Loop through each letter in the word
                if j == msgw[i][-1]:                                            # Check if it's the last letter of the word
                    flag_image = Image.open(flag_men[letters4.index(j)])        # Flag image for last letter
                    dancing_men_images.append(flag_image.resize((36, 54)))      # Resize and append image
                else:
                    man_image = Image.open(men[letters4.index(j)])              # Regular image for non-final letters
                    dancing_men_images.append(man_image.resize((36, 54)))       # Resize and append image
                count += 1

                                                                                # Create a new image for the entire encoded message
        total_width = 36 * count                                                # Calculate total width based on the number of images
        concatImage = Image.new('RGBA', (total_width, 54), (255, 255, 255, 0))  # Transparent background
        x_offset = 0

        for image in dancing_men_images:                                        # Concatenate all the images horizontally
            concatImage.paste(image, (x_offset, 0))                             # Paste image at the current offset
            x_offset += 36                                                      # Update offset for next image

        sleep(0.5)
        concatImage.save("encoded_message.png")                                 # Save the encoded image
        concatImage.show()                                                      # Display the image

        path = path.abspath("encoded_message.png")                              # Display the path where the image is saved
        print(f'\nThe enocded message has been saved to {path}\n')

        input('Press "Enter to continue... ')                                   # Wait for user to press Enter
        d = '0'                                                                 # Reset option to continue

    elif d == '2':                                                              # Option to exit
        print("Thanks for using this program :)")                               # Exit the program
        sleep(1)
        exit()
