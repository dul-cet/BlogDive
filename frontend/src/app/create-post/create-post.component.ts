import { Component } from '@angular/core';
import { ApiService } from '../services/api.service'; // путь может отличаться
import { FormsModule } from '@angular/forms';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-create-post',
  standalone: true,
  imports: [FormsModule, CommonModule],
  templateUrl: './create-post.component.html',
  styleUrls: ['./create-post.component.css']
})
export class CreatePostComponent {
  postTitle = '';
  postContent = '';

  constructor(private apiService: ApiService) {}

  createPost() {
    this.apiService.createPost(this.postTitle, this.postContent).subscribe({
      next: () => alert('Пост успешно создан!'),
      error: err => alert(err)
    });
  }
}
