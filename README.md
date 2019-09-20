# การเตรียมข้อมูลสำหรับบทความ codeforthailand's [Local Administrative Budget and Project][url]

## ที่มาของข้อมูล

ชุดข้อมูลที่เราใช้นั้นประกอบด้วย 2 ส่วนใหญ่ๆ คือ

1. ชื่ออปท.ทั้งประเทศ ซึ่งเราได้มาจาก ...

    **หมายเหตุ: มีอปท. ชื่อซำ้กัน แต่อยู่ละคนละจังหวัด**

2. ฐานของมูลจากเว็บภาษีไปไหนโดยค้นหาจากชื่อ อปท. ทั้งหมดที่เรามี

## การดึงข้อมูล

ในการดึงข้อมูลเรา เราได้เขียนโปรแกรม `./scripts/scrape-projects` ต่อเข้ากับ API ของภาษีไปไหน และไล่เอาชื่อของอปท.ไปค้นหา `./output/org-list.csv` โดยระยะเวลาดึงข้อมูลนั้น ประมาณ 48 ชั่วโมง

## การทำความสะอาดและเตรียมข้อมูลสำหรับใช้งาน

หลังจากได้ข้อมูลมาแล้ว ตัวข้อมูลจะอยู่ในรูปของไฟล์ หลายๆไฟล์ โดยแต่ละไฟล์ เป็น ลิสของโปรเจ็ค ซึ่งเราต้องเอามา 

1. เราไฟล์เหล่านี้เข้าด้วยกัน โดยใช้ขั้นตอนตาม  `./notebooks/1-consolidation.ipynb` ซึ่งผลลัพธ์ที่ได้คือไฟล์ในรูปแบบ CSV ที่ แต่ละแถวคือ​โปรเจ็ค(ของอปท)
2. เมื่อได้ข้อมูลเรียบร้อยแล้ว เราทำการคำนวนค่าทางสถิติต่างๆ สำหรับเอาไปใช้แสดงผลบน[เว็บไซต์][url] ตามขั้นตอนใน `./notebooks/2-compute-statistics.ipynb`

## ปัญหาทางด้านเทคนิคสำคัญที่พบ

1. เว็บไม่สามารถลองรับการทำงานได้มาก ถ้าหาเราส่ง Request ไปพร้อมๆ กันเว็บไม่ตอบสนอง (Timeout) ซึ่งทำให้เราต้องรันทีละ Request หรือ อีกกรณีคือ ถ้าเรา Request แล้วให้ทางเว็บส่งข้อมูลกลับมา  มากกว่า 20 Records (Pagination Size) เช่น 50 เป็นต้น ตัวเว็บก็จะมีอาการไม่ตอบสนองอยู่บ่อยๆ
2. เว็บภาษีไปไหนไม่มีการบอกว่า ในแต่ละ Query มีจำนวน records ที่เกี่ยวข้องเท่าไหร่ เราต้องลองดึงๆ ไปเรื่อยๆ จนกว่าจะได้ผลลัพธ์ที่ไม่มีข้อมูล แล้วถึงหยุด

[url]: https://codeforthailand.github.io/2019-local-administrative-budget-and-projects/
