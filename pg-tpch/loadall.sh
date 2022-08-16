echo Creating database tpch...
createdb tpch
echo Creating table space for with fast random access
psql tpch -c "create tablespace fast_random_access LOCATION '/home/david/fast_random_access' WITH (random_page_cost = 1);"
echo Creating fixeddecimal extension...
psql tpch -c "create extension fixeddecimal;"
echo Building TPC-H schema...
psql tpch -f create_fixeddecimal.sql 
echo Loading TPC-H data...
time python loaddata.py
echo Clustering lineitem by l_shipdate, l_commitdate
time psql tpch -c "begin work; create table lineitem_sorted (like lineitem); insert into lineitem_sorted select * from lineitem order by l_shipdate, l_commitdate; commit; drop table lineitem; alter table lineitem_sorted rename to lineitem;"
echo Clustering orders by o_orderdate
time psql tpch -c "begin work; create table orders_sorted (like orders); insert into orders_sorted select * from orders order by o_orderdate; commit; drop table orders; alter table orders_sorted rename to orders;"
echo Clustering part by p_size
time pql tpch -c "begin work; create table part_sorted (like part); insert into part_sorted select * from part order by p_size; commit; drop table part; alter table part_sorted rename to part;"
echo Performing Vacuum freeze...
time vacuumdb --freeze --verbose --jobs=8 --table=lineitem --table=orders --table=customer --table=nation --table=part --table=partsupp --table=region --table=supplier --dbname=tpch
echo Creating indexes...
time python index_david_v11.py
echo Creating primary keys...
time psql tpch -f primary_keys.sql
echo Building foreign key constraints...
time python foreign_keys.py
echo Applying NDISTINCT fix...
psql tpch -f ndistinct-fix-100gb.sql
echo Performing ANALYZE of tpch database...
time python analyze.py
#echo Setting column store tuples and pages...
#psql tpch -c "update pg_class set reltuples = relc.reltuples from pg_class relc join pg_cstore on (relc.oid = pg_cstore.cstrelid) where pg_cstore.cststoreid = pg_class.oid;
#update pg_class set relpages = pg_relation_size(oid) / current_setting('block_size')::int where relkind = 'C';"
echo Done.

