<?php

namespace App\Http\Controllers;

use Illuminate\Support\Facades\Redirect;
use Illuminate\Http\Request;
use App\Models\User;

class LoginController extends Controller
{
    //
    public function Logar(Request $request)
    {
        // print_r($request);exit;
        // if ($request->email == User::find("$request->email", "email") and $request->password == User::find("$request->password", "password")) {

        //     return Redirect::route('getLogin');
        // }
        self::Index();
    }
    public function Index()
    {
        return view("index");
    }
}
