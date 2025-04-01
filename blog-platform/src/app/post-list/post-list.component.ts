import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-post-list',
  templateUrl: './post-list.component.html',
  styleUrls: ['./post-list.component.css'],
  standalone: true,
  imports: [CommonModule]  // ✅ Import CommonModule to use Angular pipes like 'slice'
})
export class PostListComponent {
  posts = [
    { id: 1, title: 'First Post', content: 'This is the first post content. It has more details.' },
    { id: 2, title: 'Second Post', content: 'Another interesting post about Angular features.' }
  ];

  constructor(private router: Router) {}

  viewPost(postId: number) {
    this.router.navigate(['/post', postId]);
  }
}

