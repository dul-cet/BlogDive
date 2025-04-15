import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { FormsModule } from '@angular/forms'; // обязательно
import { CommonModule } from '@angular/common'; // тоже желательно
import { ApiService } from '../../services/api.service';
import { AuthService } from '../../interceptors/auth.service';
@Component({
  selector: 'app-login',
  standalone: true, // вот это ключевое!
  imports: [FormsModule, CommonModule], // подключаем модули
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent {
  email = '';
  password = '';
  constructor(private apiService: ApiService, private router: Router) {}

  login() {
    this.apiService.login(this.email, this.password).subscribe({
      next: (res) => {
        localStorage.setItem('token', res.token); // сохраняем JWT токен
        this.router.navigate(['/dashboard']);
      },
      error: (err) => {
        alert('Ошибка входа: ' + err);
      }
    });
  }}