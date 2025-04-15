import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { catchError } from 'rxjs/operators';
import { throwError } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ApiService {

  constructor(private http: HttpClient) { }

  // Логин
  login(email: string, password: string) {
    return this.http.post<any>('/api/login', { email, password })
      .pipe(catchError(this.handleError));
  }

  // Получение всех постов
  getPosts() {
    return this.http.get<any[]>('/api/posts')
      .pipe(catchError(this.handleError));
  }

  // Получение одного поста по ID
  getPost(id: number) {
    return this.http.get<any>(`/api/posts/${id}`)
      .pipe(catchError(this.handleError));
  }

  // Создание нового поста
  createPost(title: string, content: string) {
    return this.http.post<any>('/api/posts', { title, content })
      .pipe(catchError(this.handleError));
  }

  // Обновление поста
  updatePost(id: number, title: string, content: string) {
    return this.http.put<any>(`/api/posts/${id}`, { title, content })
      .pipe(catchError(this.handleError));
  }

  // Удаление поста
  deletePost(id: number) {
    return this.http.delete<any>(`/api/posts/${id}`)
      .pipe(catchError(this.handleError));
  }

  // Обработка ошибок
  private handleError(error: any) {
    let errorMessage = 'Что-то пошло не так!';
    if (error.error instanceof ErrorEvent) {
      // Ошибка клиента
      errorMessage = `Ошибка: ${error.error.message}`;
    } else {
      // Ошибка с сервером
      errorMessage = `Сервер вернул код ошибки: ${error.status}, сообщение: ${error.message}`;
    }
    return throwError(errorMessage);
  }
}
