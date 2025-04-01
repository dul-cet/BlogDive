import { Routes } from '@angular/router';
import { HomeComponent } from './home/home.component';
import { PostListComponent } from './post-list/post-list.component';

export const routes: Routes = [
  { path: '', component: HomeComponent },
  { path: 'posts', component: PostListComponent }
];
