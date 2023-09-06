from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import math,random
import os 

class Bill_App:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("Billing System")
    
        #title
        title=Label(self.root,text="Billing System",bd=12,relief=GROOVE,bg="#074463",fg="white",font=("Times new roman",30,"bold"),pady=2).pack(fill=X)
       
        #variables
        #Cosmetics
        self.soap=IntVar()
        self.face_cream=IntVar()
        self.face_wash=IntVar()
        self.spray=IntVar()
        self.gel=IntVar()
        self.lotion=IntVar()
        
        #Grocery
        self.rice=IntVar()
        self.food_oil=IntVar()
        self.daal=IntVar()
        self.wheat=IntVar()
        self.sugar=IntVar()
        self.tea=IntVar()
        
        #Cold Drink
        self.maaza=IntVar()
        self.coca_cola=IntVar()
        self.frooti=IntVar()
        self.pepsi=IntVar()
        self.slice=IntVar()
        self.sprite=IntVar()
        
        #Total product price & Tax Variable
        self.cosmetic_price=StringVar()
        self.grocery_price=StringVar()
        self.cold_drink_price=StringVar()
        
        self.cosmetic_tax=StringVar()
        self.grocery_tax=StringVar()
        self.cold_drink_tax=StringVar()
        
        #Customer
        self.c_name=StringVar()
        self.c_phone=StringVar()
        self.bill_no=StringVar()
        x=random.randint(1000,9999)
        self.bill_no.set(str(x))
        self.search_bill=StringVar()
        self.Total_bill=StringVar()
        
        #Customer Detail Frame
        F1=LabelFrame(self.root,bd=10,relief=GROOVE,text="Customer Details",font=("Times new roman",15,"bold"),fg="gold",bg="#074463")
        F1.place(x=0,y=80,relwidth=1)
         
        #Label
        cname_lbl= Label(F1, text="Customer Name",bg="#074463",fg="white",font=("times new roman",18,"bold"))
        cname_lbl.grid(row=0,column=0,padx=20,pady=5)
        cname_txt=Entry(F1,width=15,textvariable=self.c_name,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=1,pady=5,padx=10)
        
        cphn_lbl= Label(F1, text="Customer Phone No.",bg="#074463",fg="white",font=("times new roman",18,"bold"))
        cphn_lbl.grid(row=0,column=2,padx=20,pady=5)
        cphn_txt=Entry(F1,width=15,textvariable=self.c_phone,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=3,pady=5,padx=10)
        
        c_bill_lbl= Label(F1, text="Bill Number",bg="#074463",fg="white",font=("times new roman",18,"bold"))
        c_bill_lbl.grid(row=0,column=4,padx=20,pady=5)
        c_bill__txt=Entry(F1,textvariable=self.search_bill,width=15,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=5,pady=5,padx=10)
        
        #Buttons
        bill_btn=Button(F1,text="Search",command=self.findbill,width=20,bd=7,font=("Times new roman",15,"bold")).grid(row=0,column=6,padx=10,pady=10)
       
        #Cosmetics Frame
        F2=LabelFrame(self.root,bd=10,relief=GROOVE,text="Cosmetics",font=("Times new roman",15,"bold"),fg="gold",bg="#074463")
        F2.place(x=5,y=180,width=325,height=380)
        
        #Cosmetic lbl
        co1_lbl=Label(F2,text="Bath Soap",font=("Times new roman",16,"bold"),bg="#074463",fg="lightgreen").grid(row=0,column=0,padx=10,sticky="w")
        co1_txt=Entry(F2,width=10,textvariable=self.soap,font=("Times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)
        
        co2_lbl=Label(F2,text="Face Cream",font=("Times new roman",16,"bold"),bg="#074463",fg="lightgreen").grid(row=1,column=0,padx=10,sticky="w")
        co2_cream_txt=Entry(F2,width=10,textvariable=self.face_cream,font=("Times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)
        
        co3_lbl=Label(F2,text="Face Wash",font=("Times new roman",16,"bold"),bg="#074463",fg="lightgreen").grid(row=2,column=0,padx=10,sticky="w")
        co3_txt=Entry(F2,width=10,textvariable=self.face_wash,font=("Times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)
        
        co4_lbl=Label(F2,text="Hair Spray",font=("Times new roman",16,"bold"),bg="#074463",fg="lightgreen").grid(row=3,column=0,padx=10,sticky="w")
        co4_txt=Entry(F2,width=10,textvariable=self.spray,font=("Times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)
        
        co5_lbl=Label(F2,text="Hair Gel",font=("Times new roman",16,"bold"),bg="#074463",fg="lightgreen").grid(row=4,column=0,padx=10,sticky="w")
        co5_txt=Entry(F2,width=10,textvariable=self.gel,font=("Times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)
        
        co6_lbl=Label(F2,text="Bath Lotion",font=("Times new roman",16,"bold"),bg="#074463",fg="lightgreen").grid(row=5,column=0,padx=10,sticky="w")
        co6_txt=Entry(F2,width=10,textvariable=self.lotion,font=("Times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)
        
        
        #Grocery Frame
        F3=LabelFrame(self.root,bd=10,relief=GROOVE,text="Grocery",font=("Times new roman",15,"bold"),fg="gold",bg="#074463")
        F3.place(x=340,y=180,width=325,height=380)
        
        #Grocery lbl
        g1_lbl=Label(F3,text="Rice",font=("Times new roman",16,"bold"),bg="#074463",fg="lightgreen").grid(row=0,column=0,padx=10,sticky="w")
        g1_txt=Entry(F3,width=10,textvariable=self.rice,font=("Times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)
        
        g2_lbl=Label(F3,text="Food Oil",font=("Times new roman",16,"bold"),bg="#074463",fg="lightgreen").grid(row=1,column=0,padx=10,sticky="w")
        g2_txt=Entry(F3,width=10,textvariable=self.food_oil,font=("Times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)
        
        g3_lbl=Label(F3,text="Daal",font=("Times new roman",16,"bold"),bg="#074463",fg="lightgreen").grid(row=2,column=0,padx=10,sticky="w")
        g3_txt=Entry(F3,width=10,textvariable=self.daal,font=("Times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)
        
        g4_lbl=Label(F3,text="Wheat",font=("Times new roman",16,"bold"),bg="#074463",fg="lightgreen").grid(row=3,column=0,padx=10,sticky="w")
        g4_txt=Entry(F3,width=10,textvariable=self.wheat,font=("Times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)
        
        g5_lbl=Label(F3,text="Sugar",font=("Times new roman",16,"bold"),bg="#074463",fg="lightgreen").grid(row=4,column=0,padx=10,sticky="w")
        g5_txt=Entry(F3,width=10,textvariable=self.sugar,font=("Times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)
        
        g6_lbl=Label(F3,text="Tea Powder",font=("Times new roman",16,"bold"),bg="#074463",fg="lightgreen").grid(row=5,column=0,padx=10,sticky="w")
        g6_txt=Entry(F3,width=10,textvariable=self.tea,font=("Times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)
        
        #Cold Drink Frame
        F4=LabelFrame(self.root,bd=10,relief=GROOVE,text="Cold Drinks",font=("Times new roman",15,"bold"),fg="gold",bg="#074463")
        F4.place(x=670,y=180,width=325,height=380)
        
        #Cold Drink lbl
        c1_lbl=Label(F4,text="Maaza",font=("Times new roman",16,"bold"),bg="#074463",fg="lightgreen").grid(row=0,column=0,padx=10,sticky="w")
        c1_txt=Entry(F4,width=10,textvariable=self.maaza,font=("Times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)
        
        c2_lbl=Label(F4,text="Coca Cola",font=("Times new roman",16,"bold"),bg="#074463",fg="lightgreen").grid(row=1,column=0,padx=10,sticky="w")
        c2_txt=Entry(F4,width=10,textvariable=self.coca_cola,font=("Times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)
        
        c3_lbl=Label(F4,text="Frooti",font=("Times new roman",16,"bold"),bg="#074463",fg="lightgreen").grid(row=2,column=0,padx=10,sticky="w")
        c3_txt=Entry(F4,width=10,textvariable=self.frooti,font=("Times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)
        
        c4_lbl=Label(F4,text="Pepsi",font=("Times new roman",16,"bold"),bg="#074463",fg="lightgreen").grid(row=3,column=0,padx=10,sticky="w")
        c4_txt=Entry(F4,width=10,textvariable=self.pepsi,font=("Times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)
        
        c5_lbl=Label(F4,text="Slice",font=("Times new roman",16,"bold"),bg="#074463",fg="lightgreen").grid(row=4,column=0,padx=10,sticky="w")
        c5_txt=Entry(F4,width=10,textvariable=self.slice,font=("Times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)
        
        c6_lotion_lbl=Label(F4,text="Sprite",font=("Times new roman",16,"bold"),bg="#074463",fg="lightgreen").grid(row=5,column=0,padx=10,sticky="w")
        c6_txt=Entry(F4,width=10,textvariable=self.sprite,font=("Times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)
        
        #Bill Area
        F5=LabelFrame(self.root,bd=10,relief=GROOVE)
        F5.place(x=1010,y=180,width=400,height=380)
        bill_title=Label(F5,text="Bill Area",font=("Times new roman",15,"bold"),bd=7,relief=GROOVE).pack(fill=X) 
        scrol_y=Scrollbar(F5,orient=VERTICAL)
        self.txtarea=Text(F5,yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT,fill=Y)
        scrol_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH,expand=1)
        
        
        #ButtonFrame
        F6=LabelFrame(self.root,bd=10,relief=GROOVE,text="Bill Menu",font=("Times new roman",15,"bold"),fg="gold",bg="#074463")
        F6.place(x=0,y=560,relwidth=1,height=200)
        m1=Label(F6,text="Total Cosmetic Price",bg="#074463",fg="white",font=("Times new roman",14,"bold")).grid(row=0,column=0,padx=20,pady=1,sticky="w")
        m1_txt=Entry(F6,width=18,textvariable=self.cosmetic_price,font=("Times new roman",10),bd=7,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=1)
        
        m2=Label(F6,text="Total Grocery Price",bg="#074463",fg="white",font=("Times new roman",14,"bold")).grid(row=1,column=0,padx=20,pady=1,sticky="w")
        m2_txt=Entry(F6,width=18,textvariable=self.grocery_price,font=("Times new roman",10),bd=7,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=1)

        m3=Label(F6,text="Total Cool Drink Price",bg="#074463",fg="white",font=("Times new roman",14,"bold")).grid(row=2,column=0,padx=20,pady=1,sticky="w")
        m3_txt=Entry(F6,width=18,textvariable=self.cold_drink_price,font=("Times new roman",10),bd=7,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=1)
        
        c1=Label(F6,text="Cosmetic Tax",bg="#074463",fg="white",font=("Times new roman",14,"bold")).grid(row=0,column=2,padx=20,pady=1,sticky="w")
        c1_txt=Entry(F6,width=18,textvariable=self.cosmetic_tax,font=("Times new roman",10),bd=7,relief=SUNKEN).grid(row=0,column=3,padx=10,pady=1)
        
        c2=Label(F6,text="Grocery Tax",bg="#074463",fg="white",font=("Times new roman",14,"bold")).grid(row=1,column=2,padx=20,pady=1,sticky="w")
        c2_txt=Entry(F6,width=18,textvariable=self.grocery_tax,font=("Times new roman",10),bd=7,relief=SUNKEN).grid(row=1,column=3,padx=10,pady=1)

        c3=Label(F6,text="Cold Drink Tax",bg="#074463",fg="white",font=("Times new roman",14,"bold")).grid(row=2,column=2,padx=20,pady=1,sticky="w")
        c3_txt=Entry(F6,width=18,textvariable=self.cold_drink_tax,font=("Times new roman",10),bd=7,relief=SUNKEN).grid(row=2,column=3,padx=10,pady=1)
        
        
        btn_F=Frame(F6,bd=7,relief=GROOVE)
        btn_F.place(x=740,width=765,height=105)
        
        total_btn=Button(btn_F,text="Total",command=self.total,bg="cadetblue",fg="white",bd=2,pady=15,width=15,font=("Times new roman",15)).grid(row=0,column=0,padx=5,pady=5)       
        GBill_btn=Button(btn_F,text="Generate Bill",command=self.bill_area,bg="cadetblue",fg="white",bd=2,pady=15,width=15,font=("Times new roman",15)).grid(row=0,column=1,padx=5,pady=5)
        Clear_btn=Button(btn_F,text="Clear",command=self.clear_data,bg="cadetblue",fg="white",bd=2,pady=15,width=15,font=("Times new roman",15)).grid(row=0,column=2,padx=5,pady=5)
        Exit_btn=Button(btn_F,text="Exit",command=self.Exit_app,bg="cadetblue",fg="white",bd=2,pady=15,width=15,font=("Times new roman",15)).grid(row=0,column=3,padx=5,pady=5)
        
        self.welcome_bill()
       
        
        #footer
        lbl_footer=Label(self.root,text="BS-Billing System | Developed By SUBASHINI Student of CSE\n Adhiyamaan College Of Engineering(Autonomous),Hosur",font=("times new roman",12),bg="#010c48",fg="white").pack(side=BOTTOM,fill=X)
        
    #total function
    def total(self):
        self.c_s_p=self.soap.get()*40
        self.c_fc_p=self.face_cream.get()*120
        self.c_fw_p=self.face_wash.get()*60
        self.c_hs_p=self.spray.get()*180
        self.c_hg_p=self.gel.get()*140
        self.c_bl_p=self.lotion.get()*180
        
        self.total_cosmetic_price=float(
                                    self.c_s_p+
                                    self.c_fc_p+
                                    self.c_fw_p+
                                    self.c_hs_p+
                                    self.c_hg_p+
                                    self.c_bl_p
                                   )
        self.cosmetic_price.set("Rs. "+str(self.total_cosmetic_price))
        self.c_tax=round((self.total_cosmetic_price*0.05),2)
        self.cosmetic_tax.set("RS. "+str(self.c_tax))
        
        
        self.g_r_p=self.rice.get()*40
        self.g_f_p=self.food_oil.get()*120
        self.g_d_p=self.daal.get()*60
        self.g_w_p=self.wheat.get()*180
        self.g_s_p=self.sugar.get()*140
        self.g_t_p=self.tea.get()*180
        
        self.total_grocery_price=float(
                                    self.g_r_p+
                                    self.g_f_p+
                                    self.g_d_p+
                                    self.g_w_p+
                                    self.g_s_p+
                                    self.g_t_p
                                    )
        self.grocery_price.set("Rs. "+str(self.total_grocery_price))
        self.g_tax=round((self.total_grocery_price*0.1),2)
        self.grocery_tax.set("Rs. "+str(self.g_tax))
    
    
        self.d_m_p=self.maaza.get()*60
        self.d_c_p=self.coca_cola.get()*60
        self.d_f_p=self.frooti.get()*50
        self.d_p_P=self.pepsi.get()*45
        self.d_sl_p=self.slice.get()*40
        self.d_s_p=self.sprite.get()*60
    
        self.total_cold_drink_price=float(
                                     self.d_m_p+
                                     self.d_c_p+
                                     self.d_f_p+
                                     self.d_p_P+
                                     self.d_sl_p+
                                     self.d_s_p
                                    )
        self.cold_drink_price.set("Rs. "+str(self.total_cold_drink_price))
        self.d_tax=round((self.total_cold_drink_price*0.05),2)
        self.cold_drink_tax.set("Rs. "+str(self.d_tax))
        
        self.Total_bill=float(
                            self.total_cosmetic_price+
                            self.total_grocery_price+
                            self.total_cold_drink_price+
                            self.c_tax+
                            self.g_tax+
                            self.d_tax
                            )
        
    def welcome_bill(self):
        self.txtarea.delete('1.0',END)
        self.txtarea.insert(END,"\t\t Welcome NTS Retail ")
        self.txtarea.insert(END,f"\n\t Bill Number: {self.bill_no.get()}")
        self.txtarea.insert(END,f"\n\tCustomer Name: {self.c_name.get()}")
        self.txtarea.insert(END,f"\n\tPhone Number: {self.c_phone.get()}")
        self.txtarea.insert(END,f"\n============================================")
        self.txtarea.insert(END,f"\n\tProducts\t\tQTY\tPrice")
        self.txtarea.insert(END,f"\n============================================")
        
    def bill_area(self):
        if self.c_name.get()=="" or self. c_phone.get()=="":
            messagebox.showerror("Error","Customer details are must")
        elif self.cosmetic_price.get()=="Rs. 0.0" and self.grocery_price.get()=="Rs. 0.0" and self.cold_drink_price.get()=="Rs.0.0":
             messagebox.showerror("Error","No Product Purchased")
        else:
           self.welcome_bill()
        
        #Cosmetics
        if self.soap.get()!=0:
            self.txtarea.insert(END,f"\n\t Bath Soap\t\t{self.soap.get()}\t Rs.{self.c_s_p}")
        if self.face_cream.get()!=0:
            self.txtarea.insert(END,f"\n\t Face Cream\t\t{self.face_cream.get()}\t Rs.{self.c_fc_p}")
        if self.face_wash.get()!=0:
            self.txtarea.insert(END,f"\n\t Face Wash\t\t{self.face_wash.get()}\t Rs.{self.c_fw_p}")
        if self.spray.get()!=0:
            self.txtarea.insert(END,f"\n\t Spray\t\t{self.spray.get()}\t Rs.{self.c_hs_p}")
        if self.gel.get()!=0:
            self.txtarea.insert(END,f"\n\t Gel\t\t{self.gel.get()}\t Rs.{self.c_hg_p}")
        if self.lotion.get()!=0:
            self.txtarea.insert(END,f"\n\t Lotion\t\t{self.lotion.get()}\t Rs.{self.c_bl_p}")
            
        #Grocery
        if self.rice.get()!=0:
            self.txtarea.insert(END,f"\n\t Rice\t\t{self.rice.get()}\t Rs.{self.g_r_p}")
        if self.food_oil.get()!=0:
            self.txtarea.insert(END,f"\n\t Food oil\t\t{self.food_oil.get()}\t Rs.{self.g_f_p}")
        if self.daal.get()!=0:
            self.txtarea.insert(END,f"\n\t Daal\t\t{self.daal.get()}\t Rs.{self.g_d_p}")
        if self.wheat.get()!=0:
            self.txtarea.insert(END,f"\n\t Wheat\t\t{self.wheat.get()}\t Rs.{self.g_w_p}")
        if self.sugar.get()!=0:
            self.txtarea.insert(END,f"\n\t Sugar\t\t{self.sugar.get()}\t Rs.{self.g_s_p}")
        if self.tea.get()!=0:
            self.txtarea.insert(END,f"\n\t Tea\t\t{self.tea.get()}\t Rs.{self.g_t_p}")
            
        #Cold Drink
        if self.maaza.get()!=0:
            self.txtarea.insert(END,f"\n\t Maaza\t\t{self.maaza.get()}\t Rs.{self.d_m_p}")
        if self.coca_cola.get()!=0:
            self.txtarea.insert(END,f"\n\t Coca Cola\t\t{self.coca_cola.get()}\t Rs.{self.d_c_p}")
        if self.frooti.get()!=0:
            self.txtarea.insert(END,f"\n\t Frooti\t\t{self.frooti.get()}\t Rs.{self.d_f_p}")
        if self.pepsi.get()!=0:
            self.txtarea.insert(END,f"\n\t Pepsi\t\t{self.pepsi.get()}\t Rs.{self.d_p_P}")
        if self.slice.get()!=0:
            self.txtarea.insert(END,f"\n\t Slice\t\t{self.slice.get()}\t Rs.{self.d_sl_p}")
        if self.sprite.get()!=0:
            self.txtarea.insert(END,f"\n\t Sprite\t\t{self.sprite.get()}\t Rs.{self.d_s_p}")
        
        self.txtarea.insert(END,f"\n--------------------------------------------")
        
        if self.cosmetic_tax.get()!="Rs. 0.0":
          self.txtarea.insert(END,f"\n\t Cosmetic Tax\t\t\t{self.cosmetic_tax.get()}")
          
        if self.grocery_tax.get()!="Rs. 0.0":
          self.txtarea.insert(END,f"\n\t Grocery Tax\t\t\t{self.grocery_tax.get()}")
          
        if self.cold_drink_tax.get()!="Rs. 0.0":
          self.txtarea.insert(END,f"\n\t Cold Drink Tax\t\t\t{self.cold_drink_tax.get()}")
          
        self.txtarea.insert(END,f"\n\t Total Bill\t\t\tRs.{str(self.Total_bill)}")
        self.txtarea.insert(END,f"\n--------------------------------------------")
        self.save_bill()

    def save_bill(self):
        op=messagebox.askyesno("Save Bill","Do you want to save the bill?")
        if op>0:
            self.bill_data=self.txtarea.get('1.0',END)
            f1=open("bills/"+str(self.bill_no.get())+".txt","w")
            f1.write(self.bill_data)
            f1.close()
            messagebox.showinfo("Saved",f"Bill No: {self.bill_no.get} saved Successfully")
        else:
            return
    
    def findbill(self):
        if self.search_bill.get()=="":
            messagebox.showerror("Error","Bill No. should be required",parent=self.root)
        else:
            #print(self.bill_list,self.var_invoice.get())
            if self.search_bill.get():
                #print("yes find the invoice")
                fp=open(f'bills/{self.search_bill.get()}.txt','r')
                
                self.txtarea.delete('1.0',END)
                for i in fp:
                    self.txtarea.insert(END,i)
                fp.close()
            else:
                messagebox.showerror("Error","Invalid Bill No.",parent=self.root)
                
    def clear_data(self):
        op=messagebox.askyesno("Clear","Do you really want to Clear?")
        if op>0:
            #Cosmetics
            self.soap=IntVar()
            self.face_cream.set(0)
            self.face_wash.set(0)
            self.spray.set(0)
            self.gel.set(0)
            self.lotion.set(0)
            
            #Grocery
            self.rice.set(0)
            self.food_oil.set(0)
            self.daal.set(0)
            self.wheat.set(0)
            self.sugar.set(0)
            self.tea.set(0)
            
            #Cold Drink
            self.maaza.set(0)
            self.coca_cola.set(0)
            self.frooti.set(0)
            self.pepsi.set(0)
            self.slice.set(0)
            self.sprite.set(0)
            
            #Total product price & Tax Variable
            self.cosmetic_price.set("")
            self.grocery_price.set("")
            self.cold_drink_price.set("")
            
            self.cosmetic_tax.set("")
            self.grocery_tax.set("")
            self.cold_drink_tax.set("")
            
            #Customer
            self.c_name.set("")
            self.c_phone.set("")
            self.bill_no.set("")
            x=random.randint(1000,9999)
            self.bill_no.set(str(x))
            self.search_bill.set("")
            self.welcome_bill()        
    
    def Exit_app(self):
        op=messagebox.askyesno("Exit","Do you really want to exit?")
        if op>0:
            self.root.destroy()
                
if __name__=="__main__":
    root=Tk()
    obj=Bill_App(root)
    root.mainloop()
