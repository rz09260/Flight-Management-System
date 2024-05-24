import random
import csv
import tkinter as tk
from tkinter import simpledialog, messagebox
import string

global passengers
global flight_details
passengers = {'CBQV72': ('CBQV72', 'Christine Green', 'PQR321', 'D0'), 'KKQO01': ('KKQO01', 'Richard Leonard', 'GHI246', 'C0'), 'LCWZ92': ('LCWZ92', 'Nicole Johnson', 'MNO789', 'R0'), 'TOND46': ('TOND46', 'John Munoz', 'GHI246', 'C1'), 'NNMQ82': ('NNMQ82', 'Michael Coleman', 'PQR321', 'B1'), 'UYBH28': ('UYBH28', 'Erica Baldwin', 'GHI246', 'Y2'), 'VVGN04': ('VVGN04', 'Michelle Carson', 'MNO789', 'S1'), 'GMPH19': ('GMPH19', 'Derrick Medina', 'ABC123', 'E0'), 'TUPX49': ('TUPX49', 'Robin Morrison', 'JKL135', 'R0'), 'ADAA90': ('ADAA90', 'Patrick Holland', 'XYZ456', 'T0'), 'TGZV00': ('TGZV00', 'Jessica Powell', 'XYZ456', 'I1'), 'QSZZ83': ('QSZZ83', 'Marissa Brown', 'EFG864', 'G0'), 'TDOE82': ('TDOE82', 'Janet Moore', 'PQR321', 'W2'), 'LXHR20': ('LXHR20', 'Melissa Maldonado', 'STU654', 'S0'), 'ZJIL92': ('ZJIL92', 'Gregory Rodriguez', 'EFG864', 'T1'), 'SABS10': ('SABS10', 'Melanie Allison', 'GHI246', 'Q3'), 'LSOC71': ('LSOC71', 'Stephanie Powell', 'GHI246', 'B4'), 'XPZK28': ('XPZK28', 'Jonathan Jackson', 'XYZ456', 'Z2'), 'NRHW94': ('NRHW94', 'Nicole Crawford', 'DFD324', 'V0'), 'URDC92': ('URDC92', 'Jason Rose', 'XYZ456', 'Z3'), 'BPUH70': ('BPUH70', 'Cameron Evans', 'PQR321', 'L3'), 'AKKE05': ('AKKE05', 'Karen Moore', 'STU654', 'G1'), 'BWIO71': ('BWIO71', 'Jill Torres', 'EFG864', 'A2'), 'KFYU95': ('KFYU95', 'Julian Campbell', 'GHI246', 'I5'), 'SWWJ47': ('SWWJ47', 'Elizabeth Ibarra', 'PQR321', 'H4'), 'CNDT63': ('CNDT63', 'Anita Bauer', 'MNO789', 'J2'), 'MPLI81': ('MPLI81', 'Lori Christensen', 'EFG864', 'V3'), 'DSWR44': ('DSWR44', 'Paul Nelson', 'XYZ456', 'P4'), 'TGKH09': ('TGKH09', 'Joseph Bryan', 'EFG864', 'N4'), 'XSYA09': ('XSYA09', 'Mr. Theodore Lopez', 'PQR321', 'X5'), 'YPWK17': ('YPWK17', 'Michelle Craig', 'PQR321', 'B6'), 'RESQ91': ('RESQ91', 'Sierra Bradford', 'MNO789', 'J3'), 'KEVD93': ('KEVD93', 'Mikayla Evans', 'ABC123', 'P1'), 'YHMA16': ('YHMA16', 'Katie Stewart', 'ABC123', 'L2'), 'ETJB02': ('ETJB02', 'Melissa Christian', 'JKL135', 'Q1'), 'LDOY79': ('LDOY79', 'Sylvia Wise', 'DFD324', 'J1'), 'VCMN11': ('VCMN11', 'Teresa Ramirez', 'VWX987', 'K0'), 'FYVE69': ('FYVE69', 'Travis Curry', 'EFG864', 'B5'), 'WKAD05': ('WKAD05', 'Guy Thornton', 'VWX987', 'N1'), 'GGEM20': ('GGEM20', 'Jennifer Santos', 'DFD324', 'J2'), 'HALY51': ('HALY51', 'Mia Bird', 'MNO789', 'E4'), 'BXCN50': ('BXCN50', 'Cameron Olsen', 'ABC123', 'Q3'), 'HRDX95': ('HRDX95', 'Chelsea Brooks', 'PQR321', 'N7'), 'IXSU80': ('IXSU80', 'Nicole Abbott', 'DFD324', 'O3'), 'GZET30': ('GZET30', 'Nicholas Larson', 'VWX987', 'R2'), 'UCDW44': ('UCDW44', 'Deborah Rodriguez', 'ABC123', 'N4'), 'FEZJ20': ('FEZJ20', 'Patrick Myers MD', 'VWX987', 'H3'), 'YZWS43': ('YZWS43', 'Christine Mendez', 'DFD324', 'C4'), 'MFLY38': ('MFLY38', 'Kimberly Cardenas', 'XYZ456', 'Y5'), 'MUXA32': ('MUXA32', 'Dustin Trujillo', 'EFG864', 'U6'), 'FGRH28': ('FGRH28', 'Brenda Sampson', 'STU654', 'R2'), 'OWIX73': ('OWIX73', 'Wendy Cooper', 'XYZ456', 'F6'), 'JRME67': ('JRME67', 'Dr. Ellen Morris', 'JKL135', 'R2'), 'TFED12': ('TFED12', 'Kristin Barnes', 'PQR321', 'Z8'), 'FWUL79': ('FWUL79', 'David Gallegos', 'ABC123', 'R5'), 'HLMR14': ('HLMR14', 'Kathleen Logan', 'VWX987', 'M4'), 'CWEH97': ('CWEH97', 'Ruben Patel', 'GHI246', 'D6'), 'NDFY81': ('NDFY81', 'Mary Thomas', 'MNO789', 'C5'), 'FEIN41': ('FEIN41', 'Robert Deleon', 'EFG864', 'Q7'), 'HKIQ78': ('HKIQ78', 'Warren Ortega', 'MNO789', 'L6'), 'RUON47': ('RUON47', 'Angela Hobbs', 'XYZ456', 'W7'), 'RCPX75': ('RCPX75', 'Janet Levy', 'MNO789', 'I7'), 'PWRJ67': ('PWRJ67', 'Stephen Mclean', 'JKL135', 'K3'), 'GIHG05': ('GIHG05', 'Michaela Nelson', 'EFG864', 'H8'), 'XTSX88': ('XTSX88', 'Mrs. Melissa White', 'EFG864', 'E9'), 'OYTT19': ('OYTT19', 'Susan Barton', 'PQR321', 'Z9'), 'YMEA84': ('YMEA84', 'John Williamson', 'MNO789', 'N8'), 'VGQS55': ('VGQS55', 'Mary Mays', 'GHI246', 'S7'), 'MXJC36': ('MXJC36', 'Mark Johnson', 'STU654', 'C3'), 'NJDX34': ('NJDX34', 'Donna Salas', 'GHI246', 'W8'), 'UHOG15': ('UHOG15', 'Karen Hernandez', 'PQR321', 'J10'), 'IZOZ65': ('IZOZ65', 'Nicholas Wallace', 'STU654', 'G4'), 'VOQI39': ('VOQI39', 'Michelle Walker', 'JKL135', 'X4'), 'HZKO11': ('HZKO11', 'Brandon Hayden', 'EFG864', 'Z10'), 'SWTG83': ('SWTG83', 'Heather Anderson', 'STU654', 'O5'), 'HAAB31': ('HAAB31', 'Cynthia Cole', 'ABC123', 'B6'), 'YZIT11': ('YZIT11', 'Megan Brewer', 'PQR321', 'Y11'), 'HUPG19': ('HUPG19', 'Mallory Arias', 'XYZ456', 'S8'), 'ZTRF15': ('ZTRF15', 'Ann Powell', 'ABC123', 'V7'), 'IOHK26': ('IOHK26', 'Kathy Roth', 'PQR321', 'C12'), 'XZRE80': ('XZRE80', 'Allison Walker', 'JKL135', 'R5'), 'EQVK88': ('EQVK88', 'Brandi Kelly', 'XYZ456', 'Y9'), 'XFYV65': ('XFYV65', 'Juan Lee', 'JKL135', 'L6'), 'FFOD82': ('FFOD82', 'Ashley Lee', 'STU654', 'I6'), 'JYVF24': ('JYVF24', 'Lee Martinez', 'PQR321', 'B13'), 'MBLG73': ('MBLG73', 'Aaron Murphy', 'JKL135', 'H7'), 'TVUW38': ('TVUW38', 'Erika Diaz', 'STU654', 'K7'), 'KZNN79': ('KZNN79', 'Susan Brooks', 'GHI246', 'S9'), 'PGBV23': ('PGBV23', 'Maureen Nguyen', 'MNO789', 'U9'), 'QDAP34': ('QDAP34', 'Patricia Molina', 'EFG864', 'H11'), 'JJIQ34': ('JJIQ34', 'Wesley Shepherd', 'EFG864', 'P12'), 'NAJD73': ('NAJD73', 'Melissa Lewis', 'PQR321', 'M14'), 'OMVB11': ('OMVB11', 'Benjamin Rice', 'GHI246', 'R10'), 'QDAS69': ('QDAS69', 'Ricky Shields', 'GHI246', 'M11'), 'NLKY62': ('NLKY62', 'Jacqueline Rich MD', 'JKL135', 'U8'), 'AKTW67': ('AKTW67', 'Oscar Winters', 'ABC123', 'A8'), 'ESBA83': ('ESBA83', 'Terrence Arnold', 'JKL135', 'G9'), 'JHYE93': ('JHYE93', 'David Henry', 'STU654', 'A8'), 'ZZQE62': ('ZZQE62', 'Taylor Gill', 'JKL135', 'I10'), 'OXEH15': ('OXEH15', 'Jonathan Fox', 'DFD324', 'I5')}

# reading csv file

def load_flight_details_from_csv(filename):
    with open(filename, mode='r') as file:
        reader = csv.DictReader(file)
        flight_details = {}
        for row in reader:
            passengers = [tuple(p.split(',')) if 'None' not in p else None for p in row['Passengers'].split('|')]
            flight_details[row['Flight Number']] = [
                row['Arrival Time'],
                row['Departure Time'],
                passengers,
                int(row['Passenger Count']),
                row['Destination'],
                row['Status'],
                row['Code']
            ]
    return flight_details

# Use the function to load the data
flight_details = load_flight_details_from_csv('flight_details.csv')
print(flight_details)



# queue helper functions

def Initialize(n):
  return [None] * n


def Get(list, index):
  return list[index]


def Set(list, index, value):
  list[index] = value


def Size(list):
  size = 0
  for _ in list:
    size += 1
  return size


def NumberOfElements(list):
  number = 0
  for element in list:
    if element is None:
      return number
    else:
      number += 1
  return number


def IsEmpty(list):
  return list[0] == None


def IsFull(list):
  return list[Size(list) - 1] != None


def Insert(list, index, value):
  if IsFull(list):
    return "List is full"
  l = NumberOfElements(list)
  if index < 0 or index > l:
    return "Invalid Index"
  for j in range(l, index, -1):
    list[j] = list[j - 1]
  Set(list, index, value)
  return "Element inserted successfully"


def Remove(list, index):
  if IsEmpty(list):
    return "List is empty"

  l = NumberOfElements(list)
  if index < 0 or index >= l:
    return "Invalid Index"
  for j in range(index, l - 1):
    list[j] = list[j + 1]
  list[l - 1] = None

  return "Element removed successfully"


def InsertAtStart(list, element):
  return Insert(list, 0, element)


def RemoveFromStart(list):
  return Remove(list, 0)


def enQueue(lst, item):
  x = Insert(lst, NumberOfElements(lst), item)
  return lst


def deQueue(lst):
  y = lst[0]
  RemoveFromStart(lst)
  return y, lst


def front(lst):
  z = Get(lst, 0)
  return z


def is_empty(lst):
  if IsEmpty(lst):
    return True
  return False

# 20 mins time jump function for current time display


def plus20(time_str):
  hour_str, min_str = time_str.split(":")

  hour = int(hour_str)
  min = int(min_str)

  min += 20

  # Adjust hours and minutes if necessary
  if min >= 60:
      min -= 60
      hour += 1
  if hour >= 24:
      hour = 0

  hour_str = str(hour)
  min_str = str(min)

  if hour < 10:
      hour_str = "0" + hour_str
  if min < 10:
      min_str = "0" + min_str

  return hour_str + ":" + min_str


# functions for flight delays 

def plus40(timeStr):
  hour = int(timeStr[:2])
  min = int(timeStr[3:])

  min += 40
  if min >= 60:
      min -= 60
      hour += 1

  if hour >= 24:
      hour = 0

  hour_str = str(hour) if hour >= 10 else "0" + str(hour)
  min_str = str(min) if min >= 10 else "0" + str(min)

  new_time_str = hour_str + ":" + min_str

  return new_time_str

# notify passengers

def end_notify(lst, time):
  if not is_empty(lst):
    flight, lst = deQueue(lst)
    if flight_details[flight][6] != "D":
      if flight_details[flight][6] == "N/A":
        if flight_details[flight][1] == plus20(time):
          flight_details[flight][5] = "Boarding will end in 20 minutes"
        else:
          lst = enQueue(lst, flight)
      else:
        if flight_details[flight][6] == plus20(time):
          flight_details[flight][5] = "Boarding will end in 20 minutes"

        else:
          lst = enQueue(lst, flight)
    else:
      lst = enQueue(lst, flight)



# treaps helper functions

global root
root = (None, None)


def initialize_treap():
  treap = {}
  return treap


def create_node(time, flightN):
  priority = time
  key = (flightN, priority)
  return key


def rotate_right(treap):
  new_root = treap["left"]
  treap["left"] = new_root["right"]
  new_root["right"] = treap
  return new_root


def rotate_left(treap):
  new_root = treap["right"]
  treap["right"] = new_root["left"]
  new_root["left"] = treap
  return new_root


def add_flight(treap, time, flightN):
  key = create_node(time, flightN)
  if treap == {}:
    treap["root"] = key
    treap["left"] = {}
    treap["right"] = {}
  else:
    if key < treap["root"]:
      treap["left"] = add_flight(treap["left"], time, flightN)
      if treap["left"]["root"][1] < treap["root"][1]:
        treap = rotate_right(treap)
    else:
      treap["right"] = add_flight(treap["right"], time, flightN)
      if treap["right"]["root"][1] < treap["root"][1]:
        treap = rotate_left(treap)
  return treap


def remove_flight(treap, flightN, time):
  key = (flightN, time)
  if treap == {}:
    return treap
  elif key < treap["root"]:
    treap["left"] = remove_flight(treap["left"], flightN, time)
  elif key > treap["root"]:
    treap["right"] = remove_flight(treap["right"], flightN, time)
  else:  # key == treap["root"]
    if treap["left"] == {} and treap["right"] == {}:
      treap = {}
    elif treap["left"] == {}:
      treap = treap["right"]
    elif treap["right"] == {}:
      treap = treap["left"]
    else:  # Both children exist
      # If left child's priority is less than right child's priority
      if treap["left"]["root"][1] < treap["right"]["root"][1]:
        # Rotate right
        treap = rotate_right(treap)
        # Remove the key from the right subtree
        treap["right"] = remove_flight(treap["right"], flightN, time)
      else:
        # Rotate left
        treap = rotate_left(treap)
        # Remove the key from the left subtree
        treap["left"] = remove_flight(treap["left"], flightN, time)
  return treap


def find_flight(treap, flightime):
  if treap == {}:
    print("No flight with the given time exists.")

    return None, treap
  elif treap["root"][1] == flightime:
    flightN = treap["root"][0]
    treap = remove_flight(treap, flightN, flightime)
    return flightN, treap
  elif flightime < treap["root"][0]:
    flightN, treap["left"] = find_flight(treap["left"], flightime)
  else:
    flightN, treap["right"] = find_flight(treap["right"], flightime)


  return flightN, treap

# current clock display function 

def string_time(h,m):
  
  if h < 10:
    h = "0" + str(h)
  else:
    h = str(h)

  if m < 10:
    m  = "0" + str(m)
  else:
    m = str(m)
    
  time = h + ":" + m
  messagebox.showinfo("Time:", f"time = {time}")
  return (time)

def display_time(h, m):
  h,m = increment_time()
  time = string_time(h, m)
  treapupdates(time)
  messagebox.showinfo("Time:", f"time = {time}")
  
  #MAIN

def increment_time():
  global h, m
  m += 20
  if m >= 60:
      h += 1
      m -= 60
  if h >= 24:
      h = 0
  return h, m
  
# updating treap under constant time, with updates in flight details dictionary for flight status

def treapupdates(time):
  global treap, treap_d, runway
  flightA, treap = find_flight(treap, time)
  while flightA is not None:
    print("Arrival", treap)
    if flight_details[flightA][6] == "A" or flight_details[flightA][6] == "A_D":
        treap = remove_flight(treap, flightA, time)
        delayed_time = plus40(time)
        flight_details[flightA][5] = f"Flight delayed. Old arrival time was {time}. The flight will now be arriving at {delayed_time}."
        if flight_details[flightA][6] == "A":
          flight_details[flightA][6] = "N/A"
        else:
          flight_details[flightA][6] = "D"
        treap = add_flight(treap, delayed_time,flightA)
    else:    
      runway = enQueue(runway, flightA)
      flight_details[flightA][5] = "Boarding has begun"
      treap_d = add_flight(treap_d, flight_details[flightA][1], flightA)
    flightA, treap = find_flight(treap, time)
    print("Arrival", treap)

  print("\nRUNWAY:", runway)

  for i in range(len(runway)):
    end_notify(runway, time)

  flightD, treap_d = find_flight(treap_d, time)
  while flightD is not None:
    print("treap_d", treap_d)
    if flight_details[flightD][6] == "D":
      treap_d = remove_flight(treap_d, flightD, time)
      delayed_time = plus40(time)
      flight_details[flightD][5] = f"Flight delayed. Old departure time was {time}. The flight is now scheduled to arrive at {delayed_time}."
      flight_details[flightD][6] = delayed_time
      treap_d = add_flight(treap_d, delayed_time, flightD)
    else:  
      flight_details[flightD][5] = "Flight has departed"
      treap_d = remove_flight(treap_d, flightD, time)
    flightD, treap_d = find_flight(treap_d, time)
  return (treap, treap_d, runway)




def generate_passenger_id():
  letters = string.ascii_uppercase
  digits = string.digits

  # Generate 4 random uppercase letters
  random_letters = ''.join(random.choice(letters) for _ in range(4))

  # Generate 2 random digits
  random_digits = ''.join(random.choice(digits) for _ in range(2))

  # Combine to form the passenger ID
  passenger_id = random_letters + random_digits

  return passenger_id


def generate_seatnumber(flight_number):
  print("length", len(flight_details[flight_number][2]))
  seat_number = random.choice(string.ascii_uppercase) + str(
      flight_details[flight_number][3])
  return seat_number


# GUI!!!!


def flight_book_gui():
  global flight_details, passengers
  destination = simpledialog.askstring("Destination",
                                       "Enter your destination:")
  destination=destination.lower()
  if not destination:
    return
  available = []

  for flight in flight_details:
    available_seats = flight_details[flight][2].count(None)
    if flight_details[flight][4].lower() == destination and available_seats > 0 and flight_details[flight][5] != "Flight has departed":
        available.append((flight, flight_details[flight][0], flight_details[flight][1]))
  if available:
    for f in available:
      messagebox.showinfo("Available flights", f"Flight: {f[0]}, Arrival Time: {f[1]}, Departure Time: {f[2]}.")

    flight_number = simpledialog.askstring(
        "Flight Number", "Enter the flight number: or 0 to exit \n")

    while flight_number != "0" and flight_number not in [
        f[0] for f in available
    ]:
      if flight_number == "0":
        break
      if flight_number in [f[0] for f in available]:
        break
      else:
        flight_number = simpledialog.askstring(
            "Flight number",
            "Please enter a valid flight number or 0 to exit: ")
    if flight_number == "0":
      return
    elif flight_number in [f[0] for f in available]:
      fullname = simpledialog.askstring("Name", "Enter your full name: ")
      if flight_number:
        flight_departure_time = flight_details[flight_number][1]
        flight_arrival_time = flight_details[flight_number][0]
        passenger_id = generate_passenger_id()
        seat = generate_seatnumber(flight_number)
        
        passengers[passenger_id] = (passenger_id, fullname, flight_number,
                                    seat)
        messagebox.showinfo("Boarding Pass", f"Name: {fullname}\nFlight Number: {flight_number}\nPassenger Id: {passenger_id}\nDestination: {destination}\n Seat: {seat}\n Arrival Time:{flight_arrival_time}\n Departure Time: {flight_departure_time}")

        index = int(seat[1::])
        flight_details[flight_number][2][index] = (passenger_id, False)

  else:
    messagebox.showinfo("Note","No Flights Available")
def checkIn_gui():
  passengerid = simpledialog.askstring("Check-In", "Enter your passenger ID:")
  flightid = simpledialog.askstring("Check-In", "Enter your flight number:")

  global flight_details, passengers

  if passengerid in passengers:
    passenger_name = passengers[passengerid][1]
    seatnumber = passengers[passengerid][3]
    index = int(seatnumber[1::])
    if flightid in flight_details:
      if flight_details[flightid][2][index] != None and flight_details[flightid][2][index][0] == passengerid:
        if flight_details[flightid][2][index][1] == False:
          flight_details[flightid][2][index] = (passengerid, True)
          messagebox.showinfo("Note",
            f"Passenger {passenger_name} has checked in to flight {flightid} in seat {seatnumber}."
        )
        else:
          messagebox.showinfo("Note:",
              f"Passenger {passenger_name} has already checked in to flight {flightid} in seat {seatnumber}."
        )
      else:
        messagebox.showinfo("Note",
            f"Passenger {passenger_name} does not have a booking for this flight."
        )
    else:
      messagebox.showerror("Note", f"Flight {flightid} does not exist.")
      return
  else:
    messagebox.showerror("Note", f"Passenger {passengerid} does not exist.")
    return


def check_status_gui():
  flightid = simpledialog.askstring("Check-Status",
                                    "Enter your flight number:")
  global flight_details
  if flightid in flight_details:
    messagebox.showinfo("Note", flight_details[flightid][5])


def cancel_booking_gui():
  passengerid = simpledialog.askstring("Cancellation", "Enter your passenger ID:")
  flightid = simpledialog.askstring("Cancellation", "Enter your flight ID:")

  global passengers, flight_details
  
  if passengerid in passengers:
    if flightid is not None:
      if flight_details[flightid][5] != "Flight has departed":
        if flight_details[flightid][2][int(passengers[passengerid][3][1::])][0] == passengerid:
          flight_details[flightid][2][int(passengers[passengerid][3][1::])] = None
          del passengers[passengerid]

          flight_details[flightid][3] -= 1
          messagebox.showinfo("Cancellation", "Booking canceled successfully.")
        else:
          messagebox.showerror("Cancellation", "Invalid passenger ID.")
      else:
        messagebox.showerror("Cancellation", "Booking cannot be cancelled.")
  else:
    messagebox.showerror("Cancellation", "Passenger not found.")


runway = Initialize(10)
treap = initialize_treap()
for keys in flight_details:
  treap = add_flight(treap, flight_details[keys][0], keys)

treap_d = initialize_treap()
h = 8
m = -20
root = tk.Tk()
root.title("Flight Booking System")
root.geometry("400x400")

book_button = tk.Button(root, text="Book Flight", command=lambda: flight_book_gui())
book_button.pack(pady=10)

check_in_button = tk.Button(root, text="Check In", command=lambda: checkIn_gui())
check_in_button.pack(pady=10)

check_status_button = tk.Button(root,
                                text="Check Your Status",
                                command= lambda: check_status_gui())
check_status_button.pack(pady=10)

cancel_booking_button = tk.Button(root,
                                  text="Cancel Booking",
                                  command= lambda: cancel_booking_gui())
cancel_booking_button.pack(pady=10)

show_time_button = tk.Button(root, text="Show Time", command=lambda: display_time(h, m))
show_time_button.pack(pady=10)

root.mainloop()
