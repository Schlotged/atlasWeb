document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('login-form');
    const usernameInput = document.getElementById('id_username');
    const passwordInput = document.getElementById('id_password');
    const usernameError = document.getElementById('username-error');
    const passwordError = document.getElementById('password-error');

    form.addEventListener('submit', (e) => {
        let valid = true;
        usernameError.textContent = '';
        passwordError.textContent = '';

        if (usernameInput.value.trim() === '') {
            usernameError.textContent = 'Username is required.';
            valid = false;
        }

        if (passwordInput.value.trim() === '') {
            passwordError.textContent = 'Password is required.';
            valid = false;
        }

        if (!valid) {
            e.preventDefault(); // Impede o envio do formulário se não for válido
        }
    });
});


// function isUserAuthenticated() {

//     const token = localStorage.getItem('authToken');

//     return token !== null;
// }


// if (!isUserAuthenticated()) {
//     // Redirecione o usuário para a página de login ou exiba uma mensagem
//     window.location.href = '/login'; // ou qualquer outra ação desejada
// }
