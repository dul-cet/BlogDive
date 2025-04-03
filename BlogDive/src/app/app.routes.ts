import { Routes } from '@angular/router';
import { provideRouter } from '@angular/router';
import { PostListComponent } from './post-list/post-list.component';
import { PostDetailComponent } from './post-detail/post-detail.component';
import { CreatePostComponent } from './create-post/create-post.component';
import { LoginComponent } from './login/login.component';

export const routes: Routes = [
  { path: '', component: PostListComponent },
  { path: 'post/:id', component: PostDetailComponent },
  { path: 'create', component: CreatePostComponent },
  { path: 'login', component: LoginComponent }
];