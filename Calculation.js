document.getElementById("confirmBtn").addEventListener("click", () => {
    const selected = document.querySelectorAll('input[name="opt"]:checked');

    if (selected.length === 0) {
        alert("กรุณาเลือกอย่างน้อย 1 ตัวเลือก");
        return;
    }

    let sum = 0;

    selected.forEach(item => {
        sum += Number(item.value);
    });

    // แสดงผลรวมบนหน้าเว็บ
    document.getElementById("result").textContent = sum;
});