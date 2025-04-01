import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { RouterModule } from '@angular/router';

import { AppComponent } from './app.component';
import { NavbarComponent } from './navbar/navbar.component';
import { FooterComponent } from './footer/footer.component';
import { HomeComponent } from './home/home.component';
import { PostListComponent } from './post-list/post-list.component';

import { routes } from './app.routes';

@NgModule({

  imports: [
    BrowserModule,
    RouterModule.forRoot(routes) 
  ],
  providers: []
})
export class AppModule {}
