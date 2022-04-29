# Pokemon Database

## i.	Accomplishments
Our project Pokemon Trainer Hub allows users to create and manage accounts to keep track of Pokemons’ attributes and levels. It also allows users to make their Pokemon info private so that this can be hidden for battles. Additionally, users are able to view the public information of other users to plan ahead of battles. Users could synchronize their accounts in this database with their game accounts in real life.

## ii. Usefulness
Our Trainer info relates the information of different Pokemon trainers to their training pokemons. Users could view what pokemon contain in other users’ account if they set the pokemon to be public. Users could also read Pokemon descriptions in the table pokemon for more detailed information. Users could adopt their own pokemon and design the attributes they like, which other databases cannot satisfy. 

Our applications are different from similar applications. Instead of a public database, we allow each user to create their own accounts to record the Pokemon information. It is an opportunity to show your own pokemon to other users and record the game experience. In the traditional Pokemon database, there is only general data about the attributes of different Pokemons. However, in the real game, even pokemon with the same type would differ in some attributes. In our application, since every player would have an account, the users allow representing their specialness to other players.

## iii. Data Information
We have data from users, their friends, pokemon and relationships between each entity. The relationship between users and pokemon is characterized by training. The relationship between users is characterized by friends. While additional data is needed to describe the attributes of a pokemon. 

Each user is characterized by user_id. They also have names, password, registered email and friends. The friend relationship is represented in friends table. A pokemon has attack, defense, specialAttack, and lots of other attributes. But the attribute type of a pokemon is a special attribute for a pokemon may have one or more types. We have additional tables for that. Training specifies the training relationship between an adopted pokemon and its prototype. It is similar to the pokemon table despite that a user is authorized to manipulate data in training. A public info table contains user_id, training_id, and share_info. It associates users table with training table. 

The type information contains all of the types for pokemons. Each type has a unique typeID. We make several updates to the type table. First, a type table now only has one column, type_id. The relationship between a pokemon and its types is represented by pokemon_has_types table. The same to the training table. In addition, we add another table to illustrate the against, attacking relation between types. 

## iv. Updated ER Diagram

<img width="468" alt="image" src="https://user-images.githubusercontent.com/55035176/164086432-19882580-0fd4-4352-afe5-0a1dc58c4d2c.png">



You can view our Youtube introduction [here](https://www.youtube.com/watch?v=Zz0TVae4bNk)! 
