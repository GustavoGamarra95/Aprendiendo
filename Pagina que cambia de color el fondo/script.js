document.addEventListener("DOMContentLoaded", function () {
    const corFundoInput = document.getElementById("corFundo");
    const alterarCorButton = document.getElementById("alterarCor");

    alterarCorButton.addEventListener("click", function () {
        const novaCor = corFundoInput.value;
        alterarCorDeFundo(novaCor);
    });

    function alterarCorDeFundo(novaCor) {
        document.body.style.backgroundColor = novaCor;
    }
});
