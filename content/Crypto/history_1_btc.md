Title: Cryptocurrency History: The Birth of Bitcoin
Slug: bitcoin-whitepaper
Date: 2020-08-02
Tags: crypto, $BTC, crypto history
Summary: Review the bitcoin whitepaper.

<h3>Background</h3>
<p>
In late 2008, the global financial crisis was in full swing and multiple banks were on the verge of insolvency. Lehman Brothers filed for bankruptcy and it took a historic government bailout to rescue the other financial institutions. 
In the midst of this distrust for banks and governments, on October 31, 2008 Satoshi Nakamoto released the <a href="https://bitcoin.org/bitcoin.pdf" target="_blank">bitcoin whitepaper</a>.
Most people in the crypto universe would consider this event to be the start of cryptocurrencies. 
This post I will walk through the whitepaper and delve deeper into each section. There are a total of 12 sections:

<ol>
  <li>Introduction</li>
  <li>Transactions</li>
  <li>Timestamp Server</li>
  <li>Proof-of-Work</li>
  <li>Network</li>
  <li>Incentive</li>
  <li>Reclaiming Disk Space</li>
  <li>Simplified Payment Verification</li>
  <li>Combining and Splitting Value</li>
  <li>Privacy</li>
  <li>Calculations</li>
  <li>Conclusion</li>
</ol>

</p>

<h3>Introduction</h3>
<p>
This first paragraph explains the current flaws in the electronic payments system.
As it stands, we are in a trust based system, where banks and other financial intermediaries are third parties who process payments and arbitrate disputes. 
These disputes inherently cause transactions to be reversible which creates some issues for all of the participants in a transaction, the consumer, the merchant, and the intermediaries.
<ol>
	<li>
	Intermediaries have vast power. Assuming the intermediaries are fair, this still gives them unchecked power as they are the judge, jury, and executioner of every dispute.
	There is a reason why the legal system is split to the point where multiple people performing the roles above.
	</li>
	<li>
	The consumer must share their data to both the intermediaries and merchants. The merchant bears the fraud risk and the intermediary takes on the consumer credit risk.
	To counter this, both the merchant and the intermediary will collect financial information on the customer (salary, assets, etc.) in order to asses the consumer.
	</li>
	<li>
	The consumer and merchant must pay for the additional services of the intermediary. Along with the fee to process the payment, there is a built in fee to mediate disputes.
	Currently credit card companies charge merchants approximately a 2% fee of every transaction for their many services.
	</li>
</ol>
</p>
 
<p>
Satoshi Nakamoto purposes an alternative payments system based on cryptographic proof instead of trust in a third party. 
The cryptographic proof system would revolve around irreversible transactions, which would remove the financial intermediaries, lowering the transaction costs, while still protecting the merchants from fraud.
Buyers could also be protected by escrow mechanisms.
A brief description of the new payments system is that decentralized computers verify the irreversible transactions, creating a electronic receipt (the blockchain) that all parties can view.
</p>

<h3>Transactions</h3>
<p>
Nakamoto starts off this section with the definition of an electronic coin as a chain of digital signatures, known more commonly as the blockchain. 
A blockchain is a decentralized database that stores digital transactions, but in accordance with the irreversible transactions, it only add records when transactions occur and never edits or deletes them.
</p>

<p>
The main issue with this is procedure is the double-spend problem: how can parties verify ownership and prove people are not submitted duplicate payments to multiple participants?
In the current centralized electronic system, banks have access to both buyer and seller and thus can correctly credit or debit accounts respectively.
In the cash based system this is not an issue either as people hand over cash to each other and cannot double spend, but in a decentralized system the double-spend problem is a major dilemma.
Nakamoto solves this by publicly announcing all transactions on the blockchain so all parties are aware of a coins history.
The next step would be for the parties to agree on a single transaction history, which then assigns coins to each participant.
To do this, the blockchain needs to record timestamps for each transaction.
</p>

<h3>Timestamp Server</h3>
<p>
The timestamp server is the software that timestamps each transaction by taking a section of the transaction data and adding timestamps to it to create a hash.
This hash is a complex algorithm (SHA-256) that miners solve before the transaction can be added to the blockchain. 
Note that this fixes the double-spend problem by adding a time priority to the transactions. 
If same coin is sent to multiple parties, only first transaction is the official one that all parties agree to.
</p>

<h3>Proof of Work</h3>
<p>
Because of the decentralized nature of the blockchain, multiple transactions can be created at the same time and could arrive at the network at the same time.
This in turn clogs the network and prevents validation of these transactions. 
Proof of work, also called bitcoin mining, is the action that validates the transactions on the blockchain and then adds on the new block to the other validated chain of block.
Proof of work involves the miners solving complex math equations that are hard to solve but easy to verify. [ref]This point is one of the most important tenets of the blockchain.[/ref]
To be specific, computers scan for a particular value which when hashed begins with a certain amount of zeros.
At this point, the newly created block adds reference to data from the previous block.
It is important to note that this causes the block information to be path dependent. 
If someone wanted to change something on this particular block, they would need to edit all previous blocks.
In addition, this means that older blocks are harder to change than newer ones. 

<p>
Nakamoto also mentions that the difficulty to mine a bitcoin should be a moving average to target a fixed amount of blocks per hour. 
If blocks are generated too fast, the difficulty increases and vice versa.
</p>

<h3>Network</h3>
<p>
Nakamoto lists six steps to run a node (mine bitcoin). 
<ol>
	<li>New transactions are broadcast to all nodes.</li>
	<li>Each node collects new transactions into a block.</li>
	<li>Each node works on finding a difficult proof-of-work for its block.</li>
	<li>When a node finds a proof-of-work, it broadcasts the block to all nodes.</li>
	<li>Nodes accept the block only if all transactions in it are valid and not already spent.</li>
	<li>Nodes express their acceptance of the block by working on creating the next block in the
	chain, using the hash of the accepted block as the previous hash.</li>
</ol>
It is worth reiterating that nodes always consider the longest chain to be the correct one and will work on extending it.
There are times in which two competing nodes create two different branches of the blockchain, but eventually one branch will have more blocks and become the 'correct' version.
</p>

<h3>Incentive</h3>
<p>
Bitcoin mining is expensive and the miners need to be rewarded for their service.
After a block has been successfully mined, the block miner recieved bitcoin.
Similar to gold miners who use labor and oil resources to find gold, bitcoin minters use CPU/GPU and electricity to create bitcoins.
This process is beneficial because it rewards bitcoins to those who support the network.[ref]There will only ever been 21 million bitcoins giving bitcoin deflationary characteristics.[/ref]
It serves a further purpose as a way to bring the coins into circulation as these is no central bank to print money.
There are also transaction fees paid to miners which are more incentives to keep the network running smoothly.
</p>

<p>
From another point of view, the rewards should encourage nodes to be honest.
If a dishonest miner is able to overtake the CPU power of the honest miners, he could overwrite the existing blockchain or generate new coins.
The incentives should make it more profitable to support the network and generate more coins through mining then trying to reverse transactions.
</p>

<h3>Reclaiming Disk Space</h3>
<p>
Nakamoto lists potential ways to save memory space, because chains get longer and longer as time goes on. 
He suggests a MerkleTree to compress the data by only storing the root, however also mentions that Moore's Law and the increasing of RAM could make this a moot point. 
</p>

<h3>Simplified Payment Verification</h3>
<p>
It is possible to take a shortcut and send, receive, and verify blockchain transactions without having a full node.
Nakamoto suggests a shortcut to copy a few block headers of longest proof-of-work chain, obtain the Merkle branch for transaction to block and seeing if a network node has accepted it.
</p>

<h3>Combining and Splitting Value</h3>
<p>
Transactions to same recipient can be combined for more efficient transfers. 
</p>

<h3>Privacy</h3>
<p>
Everyone will be able to see the transactions, but if the keys are anonymous, then it is hard to track.
In addition the information is encrypted so only the holder of the private key can read and understand the messages.
Nakamoto uses the stock market as an example, where the entire market knows the trade timestamp and price, but not who bought or sold the stock.
He also suggests users to create a new key for each transaction as an additional method of security.
</p>

<h3>Calculations</h3>
<p>
What is the probability that a attack on the blockchain from a dishonest miner succeeds?
It turns out that this would create a race between honest chain and attacker chain, which can be modelled like a binomial random walk. 
A success is honest chain extending lead by one block, increasing lead by +1, while a failure is attacker chain extending by one block, reducing lead by -1.
This is the gambler's ruin problem presented below:

\begin{align}
q_z &=\left
\{\begin{matrix}
1 & \text{ if p$\leq$q}\\ 
(q/p)^z & \text{ if p$>$q}
\end{matrix}\right. \\
\text{where} & \\
p &= \text{Probability an honest node finds the next block} \\
q &= \text{Probability the attacker finds the next block} \\
q_z &= \text{Probability the attacker will ever catch up from z blocks behind} \\
\end{align}
</p>

<p>
The more $p>q$, the less of a chance the attacker has to catch up. 
Given that the function is raised to the power of $z$, if there is no lucky few breaks, the probability that the attacking chain wins exponentially declines.
</p>

<h3>Conclusion</h3>
<p>
The main issue with the current payments system is that it relies too much on the blind faith of financial institutions. 
A decentralized approach based on cryptographic proof removes the need for an intermediary, however it creates other issues like the double spend problem.
The blockchain solves the double spend problem by creating a proof-of-work record with a public history of transactions.
In addition, protocols are built in to make reversing transactions computationally impractical.
Rewards are distributed to miners to facilitate the transactions.
The network is robust in its unstructured simplicity.
</p>
