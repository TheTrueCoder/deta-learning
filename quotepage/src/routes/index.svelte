<script>
	import Quote from '$lib/Quote.svelte';
import { bind, text } from 'svelte/internal';

    const endpoint = "https://starws.deta.dev/api/quotes"

    let length = 1
    let quotes = []

	async function getQuotes() {
		let response = await fetch(endpoint + "?length=" + length)
        if (response.ok) {
            let apidata = await response.json()
            quotes = apidata.quotes
            console.log(quotes)
        }
	}
</script>

<svelte:head>
	<title>Star Warz!</title>
</svelte:head>

<h1>Get your Star Wars quotes here.</h1>
<p>It's a cool movie franchise?</p>
<br />
<input type="Number" bind:value="{length}">
<button on:click={getQuotes}>Get some delicous Star Wars quotes</button>
<br />

{#each quotes as quote}
    <Quote text={quote}/>
{/each}


<style>
	:root {
		font-family: 'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode',
			Geneva, Verdana, sans-serif;
	}
</style>
