<script>
    export const prerender = true;
    import Quote from '$lib/Quote.svelte';
    import { fade } from 'svelte/transition';

    const endpoint = "https://swquotes.nrhomelab.workers.dev/api/quotes"

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
<div>
    <h3>API Uptime</h3>
    <img alt="Uptime Robot ratio (30 days)" src="https://img.shields.io/uptimerobot/ratio/m789271530-a645a23583e3ce9e6ea6b0e6">
</div>
<br />
<input type="Number" min="1" bind:value="{length}">
<button on:click={getQuotes}>Get some delicous Star Wars quotes</button>
<br />

{#each quotes as quote}
    <div transition:fade={{duration: 300}}>
        <Quote text={quote}/>
    </div>
{/each}


<style>
	:root {
		font-family: 'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode',
			Geneva, Verdana, sans-serif;
	}
</style>
