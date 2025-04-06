import { Component } from '@angular/core';
import { Router } from '@angular/router';
@Component({
  selector: 'app-login',
  imports: [FormsModule],
  templateUrl: './login.component.html',
  styleUrl: './login.component.css',
  
})
export class LoginComponent {
  email = '';
  password = '';

  constructor(private router: Router) {}

  login() {
    if (this.email === 'admin@example.com' && this.password === '1234') {
      // Успешный вход
      this.router.navigate(['/dashboard']);
    } else {
      alert('Неверный логин или пароль');
    }
  }

}
