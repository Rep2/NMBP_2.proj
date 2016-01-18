Kopirati vijesti u mongodb

mongoimport --db web --collection newsTemp --file news.json --jsonArray

Naredba stvara kolekciju newsTemp u web bazi

Naredbom:
db.newsTemp.find().sort({date: -1}).limit(10).forEach(function(x){db.news.insert(x)})

Naredba stvara index nad date poljem:

db.news.createIndex({date: 1})

stvaramo kolekciju news u kojoj se nalaze ispravno poredanih 10 vijesti

Iz terminala pokrenuti index.py

python index.py

Pokrece se web stanica na http://localhost:8082/

Na stranici su prikazane vijesti u njihovom ispravnom redosljedu i moguce je dodavati komentare.
