<div align="center">
  <img src="https://raw.githubusercontent.com/Fedrosauro/Images/main/Images/chat_logo.png"/>
  <h1></h1>
  <img src="https://img.shields.io/badge/status-active-brightgreen"/>&nbsp;&nbsp;&nbsp;&nbsp;
  <img src="https://img.shields.io/badge/firefox-fail-red?style=flat&logo=firefox"/>&nbsp;&nbsp;&nbsp;&nbsp;
  <img src="https://img.shields.io/badge/chrome-success-green?style=flat&logo=google-chrome"/>&nbsp;&nbsp;&nbsp;&nbsp;
  <img src="https://img.shields.io/badge/safari-success-green?style=flat&logo=safari"/>
</div>
<br>

This is the application project for <i>INFORMATION SYSTEMS AND SOFTWARE DESIGN</i> course. In particular we, as a team, have developed an <b><u>online global chat</u></b> in which all people with an existing account can write messages. Having an account is required to send messages but don't worry if you don't have one, with the signin page you can make a new account and then use it.

The application is composed by 4 pages:
* Login page
* Signin page
* User chat room
* Admin chat room
<br>

<h2>Login Page</h2>
In this page the user is asked to insert <code>username</code> and <code>password</code> of an existing account (possibly his account). If the credentials submitted are present in the user table, the user will be sent in the chat in a new tab. In this situation we have 2 cases:<br><br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1. <b>The user is an admin</b>: Chat Login ⟶ Admin Chat Room
<br><br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2. <b>The user is not an admin</b>: Chat Login ⟶ Admin Chat Room
<br><br>

<h2>Signin Page</h2>
This page can be accessed by the Login Page. Inside of this page you are able to create a new account providing <code>username</code>, <code>password</code> and <code>email</code>. After doing the registration a new user will be added in the user table and the user will be again prompted to the Login Page to insert the credentials.
<br><br>

<h2>User Chat Room</h2>
This page is dedicated to the users that do not have the admin power. Therefore in this page a normal user will be able to see only the messages stored in the Message table in the database and a text input to send messages. When a message is sent, in the Message table will be saved <code>content</code>, <code>user</code> <code>time</code> of the message that has just been sent.
<br><br>

<h2>Admin Chat Room</h2>
This page is almost identical to the User Chat Room with one difference. The page is splitted in 2 columns:<br><br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1. <b>Message column</b>: in which the admin can send messages in the chat
<br><br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2. <b>Delete message column</b>: in which the admin is able to delete messages from other users providing <code>username</code> and <code>time</code> of the message &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;that he wants to delete
<br><br>

<h2>Warnings ⚠️</h2>
We strongly suggest <b>not to use personal passwords</b> of real accounts when doing the registration phase. Even tough we've provided some kind of security checks for the application, a well studied SQL Injection (for example) could breach into the database and grabs information from tables.
<br><br>

<h2>Online Platform used</h2>
<p><img src="https://github.com/Fedrosauro/Images/blob/main/Images/streamlit_cloud3.png"/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
<img src="https://github.com/Fedrosauro/Images/blob/main/Images/supabase_test.png"/></p>
