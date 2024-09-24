# MigrantSchool
- MigrantSchool is a web platform for generating educational certificates for migrants, with proof stored on the blockchain. Each certificate is securely recorded on the blockchain through a transaction.
<a href="https://demo1.isaccobertoli.com/">Try Demo</a>


## Requirements:

- A page, which only administrators can access, where it is possible to assign a degree to a student.

<p align="center">
    <img width="80%" src="./asset/img/certificate_create.png">
</p>


- A page that anyone can access and enter the identification code of a degree to view all the associated      information and transaction.

<p align="center">
    <img width="80%" src="./asset/img/landingpage.png">
    <img width="80%" src="./asset/img/certificate.png">
    <img width="80%" src="./asset/img/certificate_detail.png">
    <img width="80%" src="./asset/img/txid.png">
</p>


- A logging system to store the last IP that accessed the platform for a certain administrator user, in order to display a warning message when this is different from the previous one.

<p align="center">
    <img width="80%" src="./asset/img/ip.png">
</p>



## Deployment

To deploy this project:
- Create a Virtual Environment
- Clone the repo and install requirements.txt
- Install and run the Redis DB server
- Make database migrations
- > `python manage.py runserver`.
- open `http://127.0.0.1:8000/` in browser



## Skills
Django, Redis, Goerli Testnet Python, HTML, CSS


## 🔗 Links
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/isacco-bertoli-10aa16252/)
<br/>
<a href="https://demo1.isaccobertoli.com/">Try Demo</a>
