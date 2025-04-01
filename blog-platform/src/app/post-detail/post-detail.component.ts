import { Component } from '@angular/core';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-post-detail',
  templateUrl: './post-detail.component.html',
  styleUrls: ['./post-detail.component.css']
})
export class PostDetailComponent {
  postId: number | null = null;

  constructor(private route: ActivatedRoute) {
    this.route.params.subscribe(params => {
      this.postId = params['id'];
    });
  }
}
