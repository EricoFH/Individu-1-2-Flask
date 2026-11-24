document.addEventListener("DOMContentLoaded", function () {
  const input = document.getElementById("cariMatkul");
  const tabel = document.getElementById("tabelMatkul");
  if (!input || !tabel) return;

  input.addEventListener("input", function () {
    const kata = input.value.toLowerCase();
    tabel.querySelectorAll("tbody tr").forEach(function (baris) {
      baris.style.display =
        baris.textContent.toLowerCase().includes(kata) ? "" : "none";
    });
  });
});