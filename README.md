# My Futures Monitor
#### Video Demo:  <https://youtu.be/oJ1VJ3PFhJo>
#### Using: Flask, Python, Sqlite3, HTML, CSS, Jinja.
#### Short description: a web application that monitors the price of the major stock indices from the USA and Europe
#### Description:


### **Main files**

app.py

helpers.py

project.db

**Folders:**

**static**

style.css

sky.jpg

**templates**

apology.html

login.html

register.html

index.html

usa.html

europe.html

favourites.html

dax.html

es.html

ftse.html

ftsemib.html

nq.html

rty.html

ym.html

### **Login/Registration**
This section contains a registration form in which the user has to type **Username, Email, Password,** and **Password confirmation.**

There is a login form for the already registered users, which requires a **Username** and **Password.**

In case the user does not provide any of the necessary information, the user will then be redirected to an **" error page ".**

The **error page** tries to convey to the user the possible issue:

1. Must provide username
2. Must provide password
3. Invalid username and/or password
4. Check provided information

### **Go Back button**

There is a button below called **Go back** that redirects the user back to the login form.

### **Database**

The **sqlite3 database** is composed of two tables: users and favourites.

There are four fields in **users:** id, username, hash, and email. All the information provided during user registration is stored in this table.

To keep the password safe, there is a function that creates a random 'hash' for each user.
The **favourites table** stores the list of chosen assets for each user, more on this later.

### **Homepage**

This section contains the home page.

There is a bold greeting message customized with the username of the registrant.

To display each username, both **Jinja** and **Sqlite3** were implemented.

Simple changes in the text were made with **CSS**.

Below the greet, there is a **ticker tape.**

The ticker tape shows the current value of the major stock indices (USA and Europe).

The HTML code was provided by TradingView [https://www.tradingview.com/].

The code was then adapted to the page with **CSS** syntax.

### **USA / Europe**

The navigation bar at the top contains three sections.

The first section is called **USA**.

It contains the main stock indices of the United States of America.

They are all listed in a vertical list.

The list is customized with **CSS**, the same for the **Europe** section where the main stock indices of Europe are displayed.

Both sections USA and Europe, contain an **economic calendar** on the right of the page, provided by TradingView [https://www.tradingview.com/].

The economic calendar displays the most important economic events and a short description if clicked.

### **Watch list**

At the bottom of every list, there is a **Watch List** that stores all the chosen assets by the user.

The watch list can be updated from the **Watch List section.**

A function in the back-end accesses the database and then updates the list with the name of the assets chosen by each user; **Jinja** is then used in the **HTML** file.

### **Delete button**

Below the **Watch List** there is a button that clears all the elements previously chosen by the user.

A function in the back-end accesses the database and clears all the data in the **Favourites** field.

### **Log Out**

The log-out button in the top right corner redirects the user back to the login page.