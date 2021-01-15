select date(pdate) , date(ddate) from booking
select  * from booking where  date('2020/04/01') between date(pdate) and date(ddate) 