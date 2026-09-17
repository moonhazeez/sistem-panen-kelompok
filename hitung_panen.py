# ==========================================
# MODUL 1: INPUT DATA PANEN (Anggota 1)
# ==========================================
def input_data_panen():
    nama_petani = input("Masukkan Nama Petani: ")
    berat_panen = float(input("Masukkan Total Hasil Panen (kg): "))
    harga_per_kg = float(input("Masukkan Harga per kg: Rp "))
    return nama_petani, berat_panen, harga_per_kg

print("=== SISTEM PENCATATAN HASIL PANEN DIGITAL ===")

# ==========================================
# MODUL 2: PERHITUNGAN & DISKON (Anggota 2)
# ==========================================
def hitung_total_dan_diskon(berat, harga):
    subtotal = berat * harga
    
    # Diskon 10% jika panen lebih dari atau sama dengan 100 kg
    if berat >= 100:
        diskon = subtotal * 0.10
    else:
        diskon = 0
        
    total_bayar = subtotal - diskon
    return subtotal, diskon, total_bayar

# ==========================================
# MODUL 3: CETAK LAPORAN PANEN (Anggota 3)
# ==========================================
def cetak_laporan_panen(nama, berat, subtotal, diskon, total_bayar):
    print("\n" + "="*40)
    print("        STRUK LAPORAN HASIL PANEN       ")
    print("="*40)
    print(f"Nama Petani   : {nama}")
    print(f"Total Panen   : {berat} kg")
    print(f"Subtotal      : Rp {subtotal:,.0f}")
    print(f"Diskon        : Rp {diskon:,.0f}")
    print("-" * 40)
    print(f"TOTAL DITERIMA: Rp {total_bayar:,.0f}")
    print("="*40)

# ------------------------------------------
# JALANKAN PROGRAM UTAMA
# ------------------------------------------
petani, berat, harga = input_data_panen()
subtotal, diskon, total = hitung_total_dan_diskon(berat, harga)
cetak_laporan_panen(petani, berat, subtotal, diskon, total)
# AKHIR LAPORAN

