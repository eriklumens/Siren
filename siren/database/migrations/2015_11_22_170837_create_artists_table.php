<?php

use Illuminate\Database\Schema\Blueprint;
use Illuminate\Database\Migrations\Migration;

class CreateArtistsTable extends Migration
{
    /**
     * Run the migrations.
     *
     * @return void
     */
    public function up()
    {
        Schema::create('artists', function (Blueprint $table) {
            $table->increments('id');
            $table->string('name');
            $table->string('airline');
            $table->timestamps();

            id 				integer NOT NULL,
            name 			text NOT NULL,
            realname 		text,
            urls 			text[],
            namevariations 	text[],
            aliases 		text[],
            releases 		integer[],
            profile 		text,
            members 		text[],
            groups 			text[],
        	  data_quality 	text
        });
    }

    /**
     * Reverse the migrations.
     *
     * @return void
     */
    public function down()
    {
        //
    }
}
