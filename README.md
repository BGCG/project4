### Strategy plane

With UX principles in mind, I wanted to address what target audience the site would serve, what are their goals and what are their concerns. With this in mind, I found that I wanted to create a vegan recipe site that was all inclusive and also had varying difficulties to cater to people of all cooking confidences. I also wanted to create a community recipes site to address the lack of support an individual can sometimes feel when they are switching to a complete or partial plant-based diet.

## Target audience

* Anyone who would like to convert partially or completely to a plant-based diet
* Is open to sharing their own recipes
* Is open to interacting with others on the site via comments

## Site goals 

* To provide a wide range of plant-based recipes
* To provide a community platform where users can interact through commenting on recipes and joining the social media groups
* To provide a platform for food influencers to share their recipes and promote their following on other platforms

### New user goals

* To browse the site for vegan recipes
* To register to the site to post own recipes
* To interact with other members through commenting of recipes
* To connect to the VeggieBytes social media groups

### Current user goals

* To browse the site for newly posted vegan recipes
* To post own recipes
* To interact with other members through commenting of recipes
* To provide a platform to share their own recipes and build there account (note: this could be particularly useful for Food influencers)

### Superuser goals

* To be able to post recipes from the Admin team
* To be able to moderate post content
* To be able to moderate comments
* To filter through recipes and comments to ensure can ease the process of moderating site

### Design

#### Logo

The logo displays the name of the site in Caveat, which is a handwriting family provided by Google Fonts. It has a very organic look to represent the leaves of certain vegetables or sprouts from a plant. The font is coloured in green to further add to this organic theme.

#### Imagery

The imagery is all of different dishes where I selected those that displayed bursts of color as I wanted to create a contrast with the white background of the body of the site.

#### Colour scheme

The colour scheme represents the greenness of certain fruits and vegetables, while also sporting some bursts of colors (such as various shades of oranges, reds, pink) from the imagery used in the site, all contrasting with the white background of the site. 

### Agile epics

#### **Completed user stories**

The project was planned and carried out using the Agile methodology, making use of the GitHub Kanban boards. 

User stories were separated into MUST HAVE, SHOULD HAVE, COULD HAVE AND SHOULDN'T HAVE.

The epics were categorised in a number of different milestones - Account, Admin, Browsing, Content observation, Content creation, Content reaction.

The full Kanban board can be viewed [here](https://github.com/users/BGCG/projects/6/views/1)

In the Kanban board the user stories were divided into three sections
* No status
* To do 
* In progress 
* Done

The list of completed epics in their milestones categories are below - 

Epic | ADMIN 

* As a site admin I can moderate user comments so that I can remove any inappropriate comments (MUST HAVE)
* As a site admin I can approve or disapprove recipe posts so I can manage inappropriate content (MUST HAVE)
* As a site admin I can create, update and delete posts so that I can manage all the blog content (MUST HAVE)

Epic | ACCOUNT 

* As a site user I can login or logout of my account so that I can post recipes and react to content (MUST HAVE)
* As a site user I can set up an account so that they can like/unlike and comment on posts (MUST HAVE)

Epic | BROWSING 

* As a site user I can favourite a recipe so that I can save my favourite recipes to revisit later (MUST HAVE)

Epic | CONTENT REACTION 

* As a site user who is registered I can comment on a recipe post so that I can participate in the conversation (MUST HAVE)
* As a site user I can like/unlike recipe posts so that I can react to content (MUST HAVE)

Epic | CONTENT OBSERVATION 

* As a site user I can view how many favourites a recipe has so I can see which is the most popular (MUST HAVE)
* As a site user I can view comments so that I can observe the conversation (MUST HAVE)
* As a site user I can view number of likes on each recipe so that I can see which recipe is the most popular (MUST HAVE)
* As a site user I can open a recipe post so that I can read the recipe post (MUST HAVE)
* As a site user I can view a list of recipe posts so that I can select which one I want to read (MUST HAVE)

Epics | CONTENT CREATION 

* As a site user I can view my own post list so that I can easily access my own posts and edit them if I want (SHOULD HAVE)
* As a site admin/site user I can create drafts of recipe posts so that I can finish writing a post later (MUST HAVE)
* As a site user I can create, update and delete recipe my posts so that I can control the recipe blog content that I have posted (MUST HAVE)

#### **Uncompleted epics**

There were a few epics I did not complete. I have provided details of these and reasons for not completing them below

Epic | BROWSING 
* As a site user I can search the recipes on the site so that I can easily navigate to recipes I want to view (COULD HAVE)

Epic | ACCOUNT 
* As a registered site user I can create a user profile page so I can build a public profile to connect better with other users (COULD HAVE)

Reason for non-completion of both above epics: Time constraints

Epic | CONTENT REACTION 
* As a site user I can update and delete my own comments so I can manage my own comments if I'm not happy with them (SHOULDN'T HAVE)

Reason for non-completion: In the project inception, I thought the ability for users to have more control over their comment reactions might be a good feature for user experience. However, when inserting this user story into the Kanban board I realised that the ability of users to delete comments might disrupt the flow of the conversation so I decided it shouldn't be implemented.

### Common features

### Logo 

* The logo on the left-hand corner of each page displays the title of the site in the characteristic green colour present throughout the site.

### Navigation dropdown bar

* Is present on the top right-hand corner of each page providing navigation to authentication/signup features and home
* If logged in it provides routes to:
 - users published and draft posts ('your posts list') - which also contains links to 'Edit post' pages where a user can update their post or delete it.
 - users 'favourites list' 
 - create a post form

### Footer 

* Contains social media links to the VeggieBytes community social media accounts (just links to the social media sites as the VeggieBytes social media accounts don't exist)

### Features 

#### Homepage

* Homepage contains the site logo, navigation dropdown and welcome text explaining purpose of the site
* Contains the recently posted recipes on the site in a card format, displaying the recipe picture, title, publication date 
* When the recipe title is clicked it will take the user to the specific recipe detail page

#### Recipe detail page

* Shows all details of the recipes in a large recipe card - title, publication date, author, recipe image, ingredients, instructions, taste type, skill level and preparation time.
* Just prior to the end of the recipe card there is a like and favourite button - which is only active for logged in users. The number of likes and favourites for that post will appear next to the respective buttons.
* Furthermore, for logged in users there will be a comment box where they can post a comment. When they post a comment a message will come up showing 'Your post is awaiting approval'.
* For non-logged in users a help text will show 'If you wish to like, favourite or comment on this recipe please login or signup'. 'Login' and 'Signup' in the help text will contain links to the login or signup pages, respectively.

#### Your post list

* Has a list of published recipes (in the format of recipe cards) that the logged in user has posted 
* Additionally the your post list page has a list of draft recipes (in the format of recipe cards) written by the logged in user
* Inside both the published recipes and draft posts recipe cards has an 'Edit post' link which takes them to the edit post page for that particular post/draft

#### Create a post

* Logged in users will be able to fill out a form to submit their own recipe posts.
* They can either set the status of the post to draft or published.
* If the post is set to draft, it will be saved in your posts list, where knowone except the user (and admin in the admin panel) can see.
* If the post is set to Published and once Admin approves it, it will be visible on the homepage.

#### Edit post page

* Once the user has clicked on the 'Edit post' link on the 'Your posts page', they will be taken to the edit post page where they can edit all fields of the recipe.
* The user can also delete the post if they wish here, which a pop up box will show to make them confirm whether they do in fact wish to delete the post/draft.

### Your favourites list

* All recipes that the user has favourited will appear here in the form of recipe cards
* If the user clicks on the recipe card link the user is taken to that particular recipe

### Logout

* For authenticated users, they can click on logout in the dropdown navigation and be taken to the logout page where they will be asked to confirm if they want to logout.

### Login 

* For unauthenticated users, they can access the login page in the navigation bar which will take them to the login page where they can input their username and password.
* If their username or password is incorrect, they will be informed that their details are invalid.

### Register

* Users can create an account on the register page (accessed in the nav dropdown for unauthenticated users), where they can fill out and submit a form with their desired username, optional email and password (must enter password twice for validation).
* If their username has already been taken they will be asked to provide new details.
* Once they submit a form they will be redirected to the login page where they will be asked to login with their newly created login details.
