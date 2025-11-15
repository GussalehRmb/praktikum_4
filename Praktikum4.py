data_mahasiswa = []

while True:
    print("\n=== Input Data Mahasiswa ===")
    
    nama = input("Nama: ")
    nim = input("NIM: ")
    tugas = float(input("Nilai Tugas (30%): "))
    uts = float(input("Nilai UTS (35%): "))
    uas = float(input("Nilai UAS (35%): "))
    
    nilai_akhir = (tugas * 0.30) + (uts * 0.35) + (uas * 0.35)
    data_mahasiswa.append({
        "nama": nama,
        "nim": nim,
        "tugas": tugas,
        "uts": uts,
        "uas": uas,
        "nilai_akhir": nilai_akhir
    })
    
    lanjut = input("\nTambah data lagi? (y/t): ").lower()
    if lanjut == "t":
        break
print("="*60)
print(f"{'No':<5} {'Nama':<15} {'NIM':<10} {'Tugas':<8} {'UTS':<8} {'UAS':<8} {'Akhir':<8}")
print("="*60)

for i, mhs in enumerate(data_mahasiswa, start=1):
    print(f"{i:<5} {mhs['nama']:<15} {mhs['nim']:<10} {mhs['tugas']:<8.0f} {mhs['uts']:<8.0f} {mhs['uas']:<8.0f} {mhs['nilai_akhir']:<8.1f}")

print("="*60)