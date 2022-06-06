## Running Locally
- make sure you've python environment set up
- ```git clone https://github.com/aakzsh/colorway```
- Move to the root of the project
- ```pip install -r requirements.txt```
- ```flask run```
the app should be up and running on port 5000


## Inspiration

<img src="https://media.discordapp.net/attachments/873911768534114314/983393147121991720/Mask_group.png" width="100%"/>
Color blindness is a condition in which the ability to distinguish between certain colours is reduced. Now why is this information relevant to us? Because more than 300 million people in the world have color blindness, which is not a small number. It affects approximately 1 in 12 men and 1 in 200 women. The numbers are enough to tell that we must make sure that the world is equally accessible for people facing color blindness. There are a lot of challenges that are being faced by these people, and in our project, we tried to take a look upon them and solve a very common problem through the use and utilization of Machine Learning and Microsoft Azure services. And that is how we came up with our project, 🎇 Colorway 🎇, finding an alternative colorful way to perceive things.

## Case Studies 
<img src="https://media.discordapp.net/attachments/873911768534114314/983393147121991720/Mask_group.png" width="100%"/>

- Fashion Shopping <br>
```"Shopping for clothing is one of the more problematic experiences for the colorblind. It brings together some of the most fundamental problems of being color blind. The inability to know the exact color of clothes is frustrating. Here is what a person with color blindness has to say about their experience with shopping clothes. Some time ago I found a shirt I liked, it looked either green or gray to me. I knew that the name of the color is sometimes listed on the price tag, so I checked. In this case it was ‘asphalt’. As I was reading it I realized that I had never thought about the actual color of asphalt. Green, black or maybe gray? Suddenly buying this shirt came to be about one of the great questions of life: what color is asphalt? First you have to decide on the general color category. I decided on gray, reasoning that buildings are gray and nature is green. Asphalt isn’t part of nature, so I reckoned there was a big chance it wasn’t green but gray. But this careful consideration can only take you so far. It’s an error prone process that relies on previously learned knowledge that’s often incorrect. So my working theory was gray, but with all my deduction and reasoning I could still not be sure this was actually true. That’s because green, gray and blue belong – for most colorblind – to the same category. I might not see it all the time, but green is not gray. There’s a world of difference between them."```<br>
resource:  [We are the color blind](https://wearecolorblind.com/articles/why-buying-clothes-is-frustrating-for-the-colorblind/)

<img src="https://media.discordapp.net/attachments/873911768534114314/983393147121991720/Mask_group.png" width="100%"/>

2. Cooking and Shopping for Food<br>
Although colour blind people do develop strategies to help them cope, shopping for fruit and vegetables can be a real problem. Colour blind people often have to learn that ripe apples are often darker than unripe apples and that generally ripe fruit feels softer than unripe fruit and smells different. Here is what a research paper writer has to say about their research. <br> 
```"A good number of both protans and deutans remarked that they were unable to rely on the observation of colour change to decide when meat was cooked but used alternative strategies such as observing texture, cutting the meat, and relying on cooking time. Almost equal numbers of protans and deutans reported difficulty determining the ripeness of fruit and vegetables by judgment of colour. Bananas, apples, and tomatoes were cited as causing the most confusion and subjects reported using touch and smell to decide on ripeness."```<br>
resource: [Color blind awareness](https://www.colourblindawareness.org/colour-blindness/living-with-colour-vision-deficiency/food/)

<img src="https://media.discordapp.net/attachments/873911768534114314/983393147121991720/Mask_group.png" width="100%"/>

So what do these case studies point at? At a very repeated phenomenon. If the people can know the color, specifically an easier name of the color, without having to depend upon its darkness as they perceive it, it'll be a lot easier for them to carry out their everyday tasks. With that very specific focus, we've come up with colorway.

## What it does
<img src="https://media.discordapp.net/attachments/873911768534114314/983393147121991720/Mask_group.png" width="100%"/>
Colorway is a web application. The UI is completely color blindness friendly to let people use it feasibly. So what the app does is that, you'll be uploading an image, the app would extract the 5 major colors in the image using machine learning algorithms that have been implemented, and then it'll present the results to the users. The colors would be marked with their closest names through which a user can match it and understand what exactly that color is. The UI/UX of the app is kept simple on purpose to make it easily usable in any situation, and we feel that it is really helpful for people having color blindness. <br><br>
<img src="https://media.discordapp.net/attachments/873911460055642152/983395721929699417/unknown.png" width="400px"/>
<br><br>
<img src="https://media.discordapp.net/attachments/873911460055642152/983395263219638302/unknown.png" width="400px"/>
<br>
## How we built it
<img src="https://media.discordapp.net/attachments/873911768534114314/983393147121991720/Mask_group.png" width="100%"/>
We built the whole application step wise
- First of all, we decided how should it work, and how should it appear, means the UI/UX of colorway. Once the UI/UX was kinda finalised we moved ahead.
- We decided upon what libraries would we need, and what Azure services are gonna help us out to make our app working.
- For making the machine learning part, we used the infamous algorithm of K-means clustering, through which we were finding out the closest color which would match with each pixel of the image, and then we stored the top 5 into an array and returned that as our prediction. The algorithm was tested and writted on Azure's machine learning provided notebooks.
- The web application was made in flask. Now, there are many reasons why we used flask. Flask is lightweight, its fast and efficient, its python based so working on machine learning projects is really feasible, the framework has very easy methods for making requests and provides a very good server support. 
- For the UI part of the application, we used HTML5 and CSS3
- For getting the name of the color, we used a python's library called webcolors. Although, there was one major problem with it. It would only show the colors that are named in official CSS3, and the others would just throw error. So, to get it working, we found the closest named color to the detected color, and returned that to our user.
- We deployed our flask application on Azure's functions, which was really seamless and kinda easy in a way.

## Resources
- https://wearecolorblind.com
- https://www.colourblindawareness.org
- https://medium.com/codex/rgb-to-color-names-in-python-the-robust-way-ec4a9d97a01f
- https://towardsdatascience.com/a-step-by-step-tutorial-using-k-means-to-extract-image-color-themes-43e04808b2be

